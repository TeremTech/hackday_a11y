import time
from selenium import webdriver
from selenium_axe_python import Axe
from scraper import crawlsite
from config import url
from report_generator import generate_html_report, generate_html_report_footer, generate_html_report_header, generate_html_report_summary
from report_modifier import modify_cleanup, modify_processed, modify_progress, modify_remaining, modify_violations


def main():
    start_time = time.time()
    urls = [url]
    generate_html_report_header()
    driver = webdriver.Firefox()
    urls = crawlsite(url)
    print(urls)
    generate_html_report_summary()
    total_violations = 0
    for a in urls:
        driver.get(a)
        axe = Axe(driver)
        # Inject axe-core javascript into page.
        axe.inject()
        # Run axe accessibility checks.
        results = axe.run()
        results['url'] = a
        print()
        print("about to write for " + results['url'])
        # Write results to jsfile
        axe.write_results(results, 'a11y.json')
        generate_html_report(str(results))
        print(f"progress to {str((urls.index(a) + 1) / len(urls) * 100)}")
        modify_progress((urls.index(a) + 1) / len(urls) * 100)
        modify_processed(urls.index(a) + 1)
        modify_remaining(len(urls) - (urls.index(a) + 1))
        for issue in results['violations']:
            total_violations += len(issue['nodes'])
        modify_violations(total_violations)
    modify_processed(len(urls))
    generate_html_report_footer()
    modify_cleanup()
    driver.close()

    elapsed_time = time.time() - start_time

    print(elapsed_time)

    # need to
    # crawl website
    # get list of all URLS
    # run axe on all of them


if __name__ == "__main__":
    main()
