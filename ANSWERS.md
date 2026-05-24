1. HOW TO RUN

Generate logs:

python scripts/generator.py

Run analyzer:

python main.py

Then enter:
generated.log


2. STACK CHOICE

I used Python because it is simple and very good for text processing and file handling.


3. ONE REAL EDGE CASE

The parser correctly handles blank lines and malformed log entries without crashing.

This is handled in parser.py where invalid lines return None.


4. AI USAGE

I used ChatGPT to help understand the assignment requirements and improve parser logic.
I modified some AI-generated code to make it simpler and easier to understand.


5. HONEST GAP

The timestamp parsing is still basic and does not fully normalize all timestamp formats.
With more time, I would improve timestamp validation and formatting.
