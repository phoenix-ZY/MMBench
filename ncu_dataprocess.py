# -*- coding: utf-8 -*-
import csv
import sys

if len(sys.argv) != 3:
    print("Usage: python script.py input_file_path output_file_path")
    sys.exit(1)

input_file_path = sys.argv[1]
output_file_path = sys.argv[2]

print("Input file path: {}".format(input_file_path))
print("Output file path: {}".format(output_file_path))

# 打开并读取输入文件
with open(input_file_path, 'r') as file:
    data = file.read()

# 提取所需数据
lines = data.split('\n')
extracted_data = []
for line in lines:
    if line.strip().startswith(('dram_', 'smsp_', 'sm_', 'gpu_', 'stall_', 'achieved_', 'ipc', 'gld_', 'gst_')):
        extracted_data.append(line.strip().split())

# 创建CSV文件并写入数据
with open(output_file_path, 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Metric', 'Unit', 'Value'])
    for item in extracted_data:
        writer.writerow(item)

# 收集和计算平均值
metric_data = {}
count_data = {}
for item in extracted_data:
    metric = item[0]
    value = float(item[2])
    if metric in metric_data:
        metric_data[metric] += value
        count_data[metric] += 1
    else:
        metric_data[metric] = value
        count_data[metric] = 1

# 计算平均值并打印结果
for metric, total_value in metric_data.items():
    count = count_data[metric]
    average_value = total_value / count
    print("Metric: {}, Average Value: {}".format(metric, average_value))