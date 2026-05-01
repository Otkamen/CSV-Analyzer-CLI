[English](#english) | [Русский](#russian)

---

<a name="english"></a>
# CSV Analyzer CLI 📊

A lightweight command-line tool for analyzing CSV files — no GUI, no Excel, just one command.

## Features

- Reads any CSV file and counts category frequencies
- Shows top N categories with percentage breakdown
- Saves report to a file
- Color-coded terminal output (progress, results, errors)
- Custom column support via `--columns` flag

## Installation

```bash
git clone https://github.com/Otkaman/CSV-Analyzer-CLI.git
cd CSV-Analyzer-CLI
```

No external dependencies — uses Python standard library only.

## Usage

```bash
python main.py <file.csv> [--columns COLUMN] [--top N] [--output FILE]
```

### Arguments

| Argument | Description | Default |
|----------|-------------|---------|
| `file` | Path to CSV file (required) | — |
| `--columns` | Column to analyze | `category` |
| `--top` | Number of top categories to show | `5` |
| `--output` | Output file path | `report.txt` |

### Examples

```bash
# Basic usage
python main.py data.csv

# Show top 3 categories from 'type' column
python main.py data.csv --columns type --top 3

# Save report to custom file
python main.py data.csv --top 10 --output results.txt
```

## Output

```
 Reading data.csv...
 Analyzing data.csv...
 Saving report to report.txt...
 Top category: Electronics - 34.20%
 Done! report saved to report.txt
```

## Project Structure

```
CSV-Analyzer-CLI/
├── main.py        # Entry point, argparse, error handling
├── parser.py      # CSV reading and validation
├── stats.py       # Counter, aggregation, report writing
├── render.py      # ANSI color output
└── exceptions.py  # Custom exceptions
```

## Error Handling

| Error | Cause |
|-------|-------|
| `FileNotFoundError` | CSV file does not exist |
| `ParseError` | File is not a `.csv` |
| `ColumnNotFoundError` | Specified column not found in CSV |

## Requirements

- Python 3.10+

---

<a name="russian"></a>
# CSV Analyzer CLI 📊

Лёгкий инструмент командной строки для анализа CSV файлов — без GUI, без Excel, одной командой.

## Возможности

- Читает любой CSV файл и считает частоту категорий
- Показывает топ N категорий с процентным распределением
- Сохраняет отчёт в файл
- Цветной вывод в терминал (прогресс, результаты, ошибки)
- Поддержка любой колонки через флаг `--columns`

## Установка

```bash
git clone https://github.com/Otkaman/CSV-Analyzer-CLI.git
cd CSV-Analyzer-CLI
```

Без внешних зависимостей — только стандартная библиотека Python.

## Использование

```bash
python main.py <file.csv> [--columns КОЛОНКА] [--top N] [--output ФАЙЛ]
```

### Аргументы

| Аргумент | Описание | По умолчанию |
|----------|----------|--------------|
| `file` | Путь к CSV файлу (обязательный) | — |
| `--columns` | Колонка для анализа | `category` |
| `--top` | Количество топ категорий | `5` |
| `--output` | Путь к файлу отчёта | `report.txt` |

### Примеры

```bash
# Базовое использование
python main.py data.csv

# Топ 3 категории из колонки 'type'
python main.py data.csv --columns type --top 3

# Сохранить отчёт в свой файл
python main.py data.csv --top 10 --output results.txt
```

## Вывод

```
 Читаем data.csv...
 Анализируем data.csv...
 Сохраняем отчёт в report.txt...
 Топ категория: Electronics - 34.20%
 Готово! Отчёт сохранён в report.txt
```

## Структура проекта

```
CSV-Analyzer-CLI/
├── main.py        # Точка входа, argparse, обработка ошибок
├── parser.py      # Чтение и валидация CSV
├── stats.py       # Counter, агрегация, запись отчёта
├── render.py      # ANSI цвета в терминале
└── exceptions.py  # Кастомные исключения
```

## Обработка ошибок

| Ошибка | Причина |
|--------|---------|
| `FileNotFoundError` | CSV файл не существует |
| `ParseError` | Файл не является `.csv` |
| `ColumnNotFoundError` | Указанная колонка не найдена в CSV |

## Требования

- Python 3.10+