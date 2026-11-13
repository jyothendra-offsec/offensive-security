# Offensive Security Lab Utilities

A collection of scripts from authorized security lab work. Start with the offline Nessus filter if you want to try a utility without connecting to a target.

## Filter a Nessus export

Python 3.10 or later is sufficient. Work on a local copy of a trusted Nessus v2 export.

~~~sh
python3 nessus_filter.py original.nessus filtered.nessus
~~~

The filter removes informational findings (severity 0), preserves other findings and host metadata, and requires a new output path. A malformed export or existing destination returns exit status 2. Compare the filtered copy with the original before importing it into a reporting tool. Use [ScanBrief](https://github.com/jyothendra-offsec/scanbrief) when you need a service inventory or comparison between scans.

## Repository guide

| Area | Where to look | Before running |
| --- | --- | --- |
| Assessment reporting | [nessus_filter.py](nessus_filter.py) | Keep the original export as evidence |
| BloodHound lab setup | [ad-launch-bloodhound.sh](ad-launch-bloodhound.sh) | Review Docker and local configuration |
| Directory lab exercises | [Active Directory](Active%20Directory) and root `ad-*.sh` files | Review target, prerequisites, dependencies and permitted scope |
| Additional utilities | Root Python and shell files | Inspect hard-coded values and expected input first |

The scripts have different dependencies and lab assumptions. The repository is a lab reference. Confirm current exam restrictions independently before relying on any tool in an exam.

[Repository license](LICENSE)

## Usage terms

Original material in this revision requires the owner's written permission for modification or redistribution. Earlier MIT releases and third-party licenses retain their terms. See [LICENSE](LICENSE).
