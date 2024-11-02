#!/bin/bash

# Функция для вычисления размера папки или файла
get_size() {
    if [ -f "$1" ]; then
        du -b "$1" | cut -f1
    elif [ -d "$1" ]; then
        du -sb "$1" | cut -f1
    fi
}

# Цикл для обхода всех файлов и папок в текущей директории
for item in *; do
    size=$(get_size "$item")
    if [ -n "$size" ]; then
       echo -e "$size\t$item"
    fi
    
# Вывод отсортированного результата в два столбца
done | sort -nr | column -t -s $'\t'

