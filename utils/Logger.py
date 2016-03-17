# coding=utf-8
# log some information

report = []


# report crash event
def log_to_report_crash(name):
    report.append("crash: "+name)


def export_carsh_report():
    print(report)