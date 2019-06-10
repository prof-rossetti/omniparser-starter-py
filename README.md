# omniparser-starter-py

Contains starter code and data for the "Omniparser" Exercise.

## Installation

Fork [this repo](https://github.com/prof-rossetti/omniparser-starter-py), then clone it to download it onto your local computer. Then navigate here from the command-line:

```sh
cd omniparser-starter-py
```

## Setup

Create and activate a new Anaconda virtual environment:

```sh
conda create -n parser-env python=3.7 # (first time only)
conda activate parser-env
```

From within the virtual environment, install any packages you think you'll need:

```sh
pip install pandas # (only if you're using pandas to parse the files)
pip install pytest
```

## Usage

After addressing the "Challenges" below to implement parsing logic in Python, you can execute any of the final versions of your parser scripts, respectively:

```sh
python omniparser/gradebook_parser.py

python omniparser/filings_index_parser.py

python omniparser/stock_prices_parser.py
```

## Testing

Run tests:

```sh
pytest
```

> NOTE: before addressing the "Challenges" below, you'll notice most of the tests are failing, but after completing the challenges, the respective tests should pass

## Challenges

Tackle these challenges in order. Commit your code to create new versions as you reach milestones along the way.

### Parsing Example Gradebooks

Run the respective test for gradebook-parsing logic:

```sh
pytest test/gradebook_parser_test.py
```

Update the logic and organizational structure of the "omniparser/gradebook_parser.py" script until all tests pass.

### Parsing SEC Filings

Run the respective test for SEC filings-parsing logic:

```sh
pytest test/filings_index_parser_test.py
```

Update the logic and organizational structure of the "omniparser/filings_index_parser.py" script until all tests pass.


### Stock Prices

Run the respective test for stock-price-parsing logic:

```sh
pytest test/stock_prices_parser_test.py
```

Update the logic and organizational structure of the "omniparser/stock_prices_parser.py" script until all tests pass.
