import json
from config import logo


def generate_html_report_header(output_file="report.html"):
    # Start the HTML content
    html_content = """
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="refresh" content="1">
        <title>Accessibility Report</title>
<style>
        /* Reset and base styles */
        body, h1, table {
            margin: 0;
            padding: 0;
            font-family: 'Arial', sans-serif;
            line-height: 1.5;
        }

        body {
            background-color: #f7f7f7;
            padding: 40px;
        }

        h1 {
            text-align: center;
            padding: 20px 0;
            background-color: #2c3e50;
            color: #ecf0f1;
            margin-bottom: 40px;
        }

        img {
            vertical-align: text-bottom;
            margin-right: 10px;
        }

        progress {
            width: 90%;
            height:40px;
        }

        progress[value] {
            -webkit-appearance: none;
            appearance: none;

            width: 90%;
            height: 40px;
        }

        progress[value]::-webkit-progress-value {
        background-image:
            -webkit-linear-gradient(-45deg,
                                    transparent 33%, rgba(0, 0, 0, .1) 33%,
                                    rgba(0,0, 0, .1) 66%, transparent 66%),
            -webkit-linear-gradient(top,
                                    rgba(255, 255, 255, .25),
                                    rgba(0, 0, 0, .25)),
            -webkit-linear-gradient(left, #09c, #f44);

            border-radius: 2px;
            background-size: 35px 20px, 100% 100%, 100% 100%;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            background-color: #fff;
            box-shadow: 0 15px 15px rgba(0, 0, 0, 0.1);
        }

        th, td {
            padding: 15px 20px;
            border-bottom: 1px solid #eaeaea;
        }

        th {
            background-color: #34495e;
            color: #ecf0f1;
        }

        a {
            color: #2980b9;
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
        }

        /* Severity styles */
        .critical {
            background-color: #e57373;
            color: white;
        }

        .serious {
            background-color: #ffab91;
            color: #333;
        }

        .moderate {
            background-color: #fff176;
            color: #333;
        }

        .minor {
            background-color: #81c784;
            color: #333;
        }
    </style>
    </head>
    """
    html_content += """
    <body>
        <h1><img src='""" + logo + """' width=120> Accessibility Report</h1>"""
    # Save the HTML content to a file
    with open(output_file, "w", encoding="utf-8") as htmlfile:
        htmlfile.write(html_content)

    print(f"Report generated and saved to {output_file}")


def generate_html_report_summary(output_file="report.html"):

    html_content = """
    <table width=250>
    <tr><th>Total violations:</th><th>0</th></tr>
    <tr><th>Pages processed:</th><th>0</th></tr>
    <tr><th>Pages remaining:</th><th>0</th></tr>
    </table><br/>
    <progress max="100" value="0"></progress>
    <hr><br/>
    """

    # Save the HTML content to a file
    with open(output_file, "a", encoding="utf-8") as htmlfile:
        htmlfile.write(html_content)

    print(f"Report generated and saved to {output_file}")


def generate_html_report(json_data, output_file="report.html"):
    # Parse the JSON data
    with open("a11y.json", "r", encoding="utf-8") as jsonfiletoread:
        json_data = jsonfiletoread.read()
    data = json.loads(json_data)
    totalcount = sum(len(issue['nodes']) for issue in data['violations'])

    # Start the HTML content
    html_content = """
        <table border="1">
            <tr>
            <td>URL</td><td>""" + data['url'] + """</td>
            <td>Violations</td><td>""" + str(totalcount) + """</td>
            </tr>
        </table>
        <p>
        <table border="1">
            <tr>
                <th>No</th>
                <th>Type</th>
                <th>Description</th>
                <th>Severity</th>
                <th>Count</th>
                <th>Help</th>
            </tr>
    """

    for i, issue in enumerate(data['violations'], start=1):
        severity_class = issue['impact']
        html_content += f"""
        <tr class="{severity_class}">
            <td>{i}</td>
            <td>{issue['id']}</td>
            <td>{issue['description']}</td>
            <td>{issue['impact']}</td>
            <td>{len(issue['nodes'])}</td>
            <td><a href='{issue['helpUrl']}'>{issue['id']}</td>
        </tr>
        """

    html_content += """</table><br>"""

    # Save the HTML content to a file
    with open(output_file, "a", encoding="utf-8") as htmlfile:
        htmlfile.write(html_content)

    print(f"Report generated and saved to {output_file}")


def generate_html_report_footer(output_file="report.html"):
    # Close the HTML tags
    html_content = """
    </body>
    </html>
    """

    # Save the HTML content to a file
    with open(output_file, "a", encoding="utf-8") as htmlfile:
        htmlfile.write(html_content)

    print(f"Report generated and saved to {output_file}")


if __name__ == "__main__":
    with open("a11y.json", "r", encoding="utf-8") as jsonfile:
        json_data_report = jsonfile.read()

    generate_html_report(json_data_report)
