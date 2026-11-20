# 山地公交的班距归因和控车试算

这里保存山地公交的班距归因和控车试算工作所用的匿名合成记录。文件不包含分析结果或居民个人资料。

## 资料

`samples/` 中每个文件都是独立的 UTF-8 JSON 文档：`schedules`、`facts`、`riders`、`site_limits`、`study`。日期是当地日历日期。空值表示没有对应观测或状态资料，不是数值零。

班次 start/到离分钟以运行日零点为基准，可以大于 1439。事实 received 是记录到达调度台的分钟；arrived 是到站分钟。同一班次的更正定位指向同日同站记录。riders 的 ready 为到候车点的可行分钟范围，via 为必须换乘的位置。控制点容量和车辆周转限制见 site_limits。

## 运行

使用 Python 3.11，无需第三方依赖或服务。`python3 inspect_samples.py` 逐个读取资料并列出记录数；`python3 -m unittest -v` 检查关键原始记录间的关系。输出只描述原始资料，不是业务比较结果。
