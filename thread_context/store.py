import threading
import time


class ConversationStore:
    """Thread-safe in-memory conversation history for OpenAI Agents SDK."""

    def __init__(self, ttl_seconds: int = 86400, max_conversations: int = 1000):
        self._store: dict[tuple[str, str], dict] = {}
        self._lock = threading.Lock()
        self._ttl_seconds = ttl_seconds
        self._max_conversations = max_conversations

    def get_history(self, channel_id: str, thread_ts: str) -> list | None:
        key = (channel_id, thread_ts)
        with self._lock:
            entry = self._store.get(key)
            if entry is None:
                return None
            if time.time() - entry["timestamp"] > self._ttl_seconds:
                del self._store[key]
                return None
            return entry["messages"]

    def set_history(self, channel_id: str, thread_ts: str, messages: list) -> None:
        key = (channel_id, thread_ts)
        with self._lock:
            self._store[key] = {"messages": messages, "timestamp": time.time()}
            self._cleanup()

    def _cleanup(self) -> None:
        now = time.time()
        expired = [
            k
            for k, v in self._store.items()
            if now - v["timestamp"] > self._ttl_seconds
        ]
        for k in expired:
            del self._store[k]
        if len(self._store) > self._max_conversations:
            sorted_keys = sorted(
                self._store.keys(), key=lambda k: self._store[k]["timestamp"]
            )
            for k in sorted_keys[: len(self._store) - self._max_conversations]:
                del self._store[k]


conversation_store = ConversationStore()

# Back-compat alias used by older imports during migration
session_store = conversation_store
