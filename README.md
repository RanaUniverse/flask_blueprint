flask --app main run --debug --host=0.0.0.0 --port=5000

flask run --debug --host=0.0.0.0 --port=5000



find . -type f \( -name "*.py" -o -name "*.toml" -o -name "*.md" -o -name "*.lock" -o -name "*.html" \) -print -exec sh -c 'echo "\n--- {} ---"; cat "{}"' \;


find . -type f \( -name "*.py" -o -name "*.html" \) \
-print -exec sh -c 'echo "\n--- {} ---"; cat "{}"' \;


flask --app rana_universe_testing run --debug --host=0.0.0.0 --port=5000
