"""Remove informational findings from a local Nessus v2 export."""
import argparse
import xml.etree.ElementTree as ET
from pathlib import Path


def filter_informational_findings(input_file, output_file):
    """Write a new report and return the number of removed entries."""
    tree = ET.parse(input_file)
    root = tree.getroot()
    if root.tag != "NessusClientData_v2":
        raise ValueError("expected a Nessus v2 XML export")
    removed = 0
    for host in root.iter("ReportHost"):
        for item in host.findall("ReportItem"):
            if item.get("severity") == "0":
                host.remove(item)
                removed += 1
    destination = Path(output_file)
    with destination.open("xb") as stream:
        try:
            tree.write(stream, encoding="utf-8", xml_declaration=True)
            stream.flush()
        except OSError:
            stream.close()
            destination.unlink(missing_ok=True)
            raise
    return removed


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path, help="New .nessus file")
    args = parser.parse_args()
    try:
        removed = filter_informational_findings(args.input, args.output)
    except (OSError, ET.ParseError, ValueError) as exc:
        parser.exit(2, f"nessus_filter: {exc}\n")
    print(f"Removed {removed} informational findings. Wrote {args.output}.")


if __name__ == "__main__":
    main()
