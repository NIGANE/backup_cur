# from rank_bm25 import BM25Okapi
import bm25s


def get_docs():
    TEST_CORPUS = [
        (
            "POSIX thread synchronization in C relies heavily on POSIX mutexes"
            " (pthread_mutex_t) and condition variables (pthread_cond_t). A mutex"
            " provides mutual exclusion to prevent race conditions when multiple"
            " threads access shared memory concurrently. Calling"
            " pthread_mutex_lock() blocks execution until the lock is acquired,"
            " while pthread_cond_wait() atomically releases the mutex and waits for"
            " a signal on the condition variable. Failing to acquire locks in a"
            " consistent order can lead to system deadlock."
        ),
        (
            "In C and C++, pointer arithmetic operates based on the data type of"
            " the pointer. Incrementing a pointer (ptr++) advances its memory"
            " address by sizeof(*ptr) bytes rather than a single raw byte address."
            " Wild pointers and dangling pointers occur when memory is uninitialized"
            " or freed via free() without setting the pointer variable to NULL."
            " Buffer overflows happen when an array index exceeds its allocated"
            " heap or stack buffer bounds."
        ),
        (
            "Enterprise network security frequently utilizes RADIUS (Remote"
            " Authentication Dial-In User Service) and LDAP (Lightweight Directory"
            " Access Protocol) for centralized authentication. RADIUS uses UDP"
            " port 1812 for authentication and UDP port 1813 for accounting. Single"
            " Sign-On (SSO) frameworks often implement SAML 2.0 or OIDC (OpenID"
            " Connect) on top of OAuth 2.0 to issue cryptographically signed JWT"
            " (JSON Web Tokens) for stateless user session management."
        ),
        (
            "Modern CPUs employ multi-level cache hierarchies consisting of L1, L2,"
            " and L3 caches to mitigate the memory wall latency gap between the CPU"
            " core and DRAM. Cache lines are typically 64 bytes wide. Spatial"
            " locality refers to accessing memory locations near recently accessed"
            " addresses, while temporal locality refers to reusing the same memory"
            " locations within a short time window. Cache invalidation protocols"
            " like MESI maintain cache coherency across multi-core processors."
        ),
        (
            "Network socket programming using POSIX sockets involves socket(),"
            " bind(), listen(), and accept() functions on the server side. TCP"
            " sockets establish a reliable, full-duplex stream using a three-way"
            " handshake (SYN, SYN-ACK, ACK), whereas UDP sockets operate in a"
            " connectionless manner using sendto() and recvfrom(). Non-blocking I/O"
            " multiplexing can be managed efficiently using epoll() on Linux or"
            " kqueue() on BSD systems."
        ),
    ]
    return TEST_CORPUS


print(f"len of the docs: {len(get_docs())}")

# 1. Lexical Tokenization (String splitting & lowercasing)
corpus_tokens = bm25s.tokenize(get_docs(), lower=True)

retriever = bm25s.BM25()
retriever.index(corpus_tokens)

# 3. Execution Phase (Done PER REQUEST)
query_text = "How do I prevent race conditions using mutex in POSIX C?"
query_tokens = bm25s.tokenize(query_text, lower=True)

# Retrieve top K=2 chunks
results, scores = retriever.retrieve(query_tokens, k=2)
# Extract top text passages
retrieved_chunks = [get_docs()[idx] for idx in results[0]]
print(len(retrieved_chunks))
# print(retrieved_chunks)
exit(1)
# 4. Prompt Injection (Formatting for LLM context window)
context_block = "\n\n".join(
    [f"[Source {i+1}]: {chunk}" for i, chunk in enumerate(retrieved_chunks)]
)

final_llm_prompt = f"""
System: You are an expert engineer. Answer the question using ONLY the provided context. If the answer cannot be found in the context, state that you do not know.

CONTEXT:
{context_block}

USER QUESTION:
{query_text}
"""

print(final_llm_prompt)