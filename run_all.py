"""Run every problem's tests and print a summary.

    python run_all.py                    # test your solutions (all topics)
    python run_all.py two_pointers       # only one topic
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
TOPICS = ["two_pointers", "sliding_window"]


def main():
    args = sys.argv[1:]
    use_ref = "--ref" in args
    chosen = [a for a in args if a in TOPICS] or TOPICS
    counts = {"PASS": 0, "FAIL": 0, "TODO": 0}

    for topic in chosen:
        print(f"\n== {topic} ==")
        topic_dir = os.path.join(ROOT, topic)
        folders = sorted(f for f in os.listdir(topic_dir)
                         if os.path.isdir(os.path.join(topic_dir, f)))
        for folder in folders:
            cmd = [sys.executable, "test.py"] + (["--ref"] if use_ref else [])
            proc = subprocess.run(cmd, cwd=os.path.join(topic_dir, folder),
                                  capture_output=True, text=True)
            output = proc.stdout + proc.stderr
            if proc.returncode == 0:
                status = "PASS"
            elif "NotImplementedError" in output:
                status = "TODO"
            else:
                status = "FAIL"
            counts[status] += 1
            print(f"  [{status}] {folder}")

    total = sum(counts.values())
    print(f"\n{counts['PASS']}/{total} passing, {counts['FAIL']} failing, {counts['TODO']} not started")
    sys.exit(1 if counts["FAIL"] else 0)


if __name__ == "__main__":
    main()
