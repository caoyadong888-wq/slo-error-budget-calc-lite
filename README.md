# SLO Error Budget Calculator (Lite)

## English

Downtime for a 30-day window and a 90-day window. A day is 86400 seconds. Availability is a percent in (0, 100].

Allowed seconds = days * 86400 * (100 - percent) / 100.

For 99.9 percent the 30-day result is 2592 seconds (43.2 minutes). The 90-day result is 7776 seconds (129.6 minutes).

This subset has no request budget, no burn rate, no policy stub, and no workbook.

### Deliverables

- `deliverables/calc_slo_lite.py` — 30-day and 90-day downtime
- `examples/target_99_9.json` — availability 99.9

### Quick start

```bash
python3 deliverables/calc_slo_lite.py --availability-percent 99.9
```

```bash
python3 deliverables/calc_slo_lite.py --scenario examples/target_99_9.json
```

Requires Python 3.9 or newer. No third-party packages.

## 中文

只计算 30 天和 90 天的允许停机时间。一天按 86400 秒。可用性是大于 0 且不超过 100 的百分比。

允许停机秒数 = 天数 * 86400 * (100 - 百分比) / 100。

99.9% 时，30 天是 2592 秒（43.2 分钟），90 天是 7776 秒（129.6 分钟）。

精简版没有请求预算、没有燃烧率、没有策略存根，也没有工作簿。

### 交付文件

- `deliverables/calc_slo_lite.py`
- `examples/target_99_9.json`

### 快速开始

```bash
python3 deliverables/calc_slo_lite.py --scenario examples/target_99_9.json
```

需要 Python 3.9 或更高版本，无第三方包。

Full version: GUMROAD_URL
