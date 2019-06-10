from omniparser.filings_index_parser import BASE_URL, find_filing_url

def test_base_url():
    assert BASE_URL == "https://www.sec.gov/Archives"

def test_find_filing_url():
    filepath = os.path.join(os.path.dirname(__file__), "..", "data", "filings_index_201903.txt")
    filing_url = find_filing_url(filepath, form_type="10-K", company_name="AMAZON COM INC")
    assert(filing_url) == "https://www.sec.gov/Archives/edgar/data/1018724/0001018724-19-000004.txt"

    prev_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "filings_index_201303.txt")
    prev_filing_url = find_filing_url(filepath, form_type="10-K", company_name="AMAZON COM INC")
    assert(prev_filing_url) == "https://www.sec.gov/Archives/edgar/data/1018724/0001193125-13-028520.txt"
