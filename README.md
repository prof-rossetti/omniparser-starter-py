# omniparser-starter-py

The "Omniparser" is a test-driven exercise in parsing data files in different formats (TXT, JSON, CSV, etc.).  

## Installation

Fork [this repo](https://github.com/prof-rossetti/omniparser-starter-py), then clone or download your forked repo onto your local computer, and navigate into its root directory from the command-line:

```sh
cd omniparser-starter-py
```

## Setup

Create and activate a new virtual environment:

```sh
conda create -n parser-env python=3.7 # (first time only)
conda activate parser-env
```

From within the virtual environment, install pytest:


```sh
pip install pytest
```

You may also install any other packages along the way which you think might help you satisfy the challenges:

```sh
pip install pandas # (for example, if you like that kind of thing)
```

## Usage

After addressing the "Challenges" below, you should be able to run any of these parser scripts, and they should work:

```sh
python omniparser/gradebook_parser.py

python omniparser/filings_index_parser.py

python omniparser/stock_prices_parser.py
```

Open any of those files and you'll see they are empty. It's up to you to write code in each parser script to satisfy the expectations set forth in its corresponding test (see "Testing", below).

## Testing

Run all the tests:

```sh
pytest
```

Before addressing the "Challenges" below, you'll notice the tests are failing. 

There is no need to edit or modify the tests in any way. After completing the "Challenges" below, all tests should pass.


## Challenges

### Gradebook Parser

Run tests for the gradebook parser:

```sh
pytest test/gradebook_parser_test.py
```

Your objective is to: **iteratively update the "omniparser/gradebook_parser.py" script and re-run these tests until all tests pass**.

### SEC Filings Index Page Parser

Run tests for the SEC filings parser:

```sh
pytest test/filings_index_parser_test.py
```

Your objective is to: **iteratively update the "omniparser/filings_index_parser.py" script and re-run these tests until all tests pass**.

### Stock Prices Parser

Run tests for the stock prices parser:

```sh
pytest test/stock_prices_parser_test.py
```

Your objective is to: **iteratively update the "omniparser/stock_prices_parser.py" script and re-run these tests until all tests pass**.

<hr>

Good luck! And I hope you enjoy these exercises. 🎉 🙌 If you'd like to contribute an update or a fix or even a new challenge to this repo, PRs are welcome!


