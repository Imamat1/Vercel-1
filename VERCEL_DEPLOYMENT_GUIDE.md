# 🚀 Инструкция по развертыванию курса на Vercel

## 📋 Подготовка завершена

### ✅ Что оптимизировано:
1. **Размер проекта**: Создан `.vercelignore` для исключения лишних файлов
2. **База данных**: Переключено на Supabase PostgreSQL
3. **Конфигурация**: Обновлены все настройки для Vercel
4. **Структура**: Подготовлена serverless архитектура

### ✅ Что настроено:
- **vercel.json** - Конфигурация для Vercel
- **api/index.py** - Точка входа для serverless функций
- **api/create_tables.py** - Скрипт создания таблиц
- **requirements.txt** - Зависимости Python
- **frontend/.env** - URL для Vercel (chasa.vercel.app)
- **backend/.env** - Конфигурация Supabase
- **.vercelignore** - Исключение лишних файлов

## 🗄️ Настройка базы данных Supabase

### 1. Создание таблиц
Выполните скрипт создания таблиц в Supabase:

```bash
cd api
python create_tables.py
```

### 2. Создание примера курса (опционально)
Для демонстрации функциональности создайте пример курса:

```bash
cd api
python create_sample_course.py
```

Это создаст курс "Основы Ислама" с 3 уроками и тестами.

### 2. Структура таблиц
Скрипт создаст следующие таблицы:
- `admin_users` - Пользователи админки
- `students` - Студенты
- `teachers` - Преподаватели
- `courses` - Курсы
- `lessons` - Уроки
- `tests` - Тесты
- `questions` - Вопросы тестов
- `test_sessions` - Сессии тестирования
- `team_members` - Команда проекта
- `qa_questions` - Вопросы и ответы имама
- `applications` - Заявки студентов
- `test_attempts` - Попытки тестов
- `status_checks` - Проверки статуса

### 3. Данные по умолчанию
Автоматически создаются:
- **Админ**: admin@uroki-islama.ru / admin123
- **Команда**: 3 члена команды по умолчанию

## 🔧 Развертывание на Vercel

### 1. Загрузка проекта
```bash
# Если используете GitHub
git add .
git commit -m "Optimized for Vercel deployment"
git push origin main
```

### 2. Настройка в Vercel Dashboard
1. Зайдите на [vercel.com](https://vercel.com)
2. Импортируйте проект из GitHub
3. Перейдите в **Settings** → **Environment Variables**
4. Добавьте переменные окружения:

```
SUPABASE_URL=https://kykzqxoxgcwqurnceslu.supabase.co
SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imt5a3pxeG94Z2N3cXVybmNlc2x1Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1MTQ4NzI0OCwiZXhwIjoyMDY3MDYzMjQ4fQ.wZcC233qDjrIuXn4it1j-YnxHak14v8GqxCCuW6VIb4
SECRET_KEY=uroki-islama-secret-key-2024
DATABASE_URL=postgresql://postgres:jsjsjdhsivdusbdis267263733673@db.kykzqxoxgcwqurnceslu.supabase.co:5432/postgres
USE_POSTGRES=true
```

### 3. Настройки проекта
- **Build Command**: оставьте пустым (по умолчанию)
- **Root Directory**: оставьте пустым
- **Install Command**: `yarn install`

### 4. Деплой
Нажмите **Deploy** для развертывания

## 🎯 Проверка после развертывания

### 1. API тесты
- **Статус**: `https://chasa.vercel.app/api/`
- **Курсы**: `https://chasa.vercel.app/api/courses`
- **Команда**: `https://chasa.vercel.app/api/team`

### 2. Админ панель
- **URL**: `https://chasa.vercel.app/`
- **Логин**: admin@uroki-islama.ru
- **Пароль**: admin123

### 3. Функции
- ✅ Создание курсов
- ✅ Управление уроками
- ✅ Система тестирования
- ✅ Загрузка файлов
- ✅ Команда проекта
- ✅ Q&A система

## 📊 Размер оптимизации

### До оптимизации:
- **Общий размер**: 489MB
- **node_modules**: 485MB
- **Причина**: Превышение лимита Vercel (250MB)

### После оптимизации:
- **Исключены**: node_modules, __pycache__, временные файлы
- **Размер**: < 5MB (без node_modules)
- **Результат**: Соответствует лимиту Vercel

## 🛠️ Техническая структура

### Frontend
- **React** приложение
- **Tailwind CSS** для стилей
- **Axios** для API запросов
- **React Router** для навигации

### Backend
- **FastAPI** как serverless функции
- **PostgreSQL** (Supabase) как БД
- **Pydantic** для валидации
- **JWT** для аутентификации

### Deployment
- **Vercel** для хостинга
- **Serverless функции** для backend
- **Static hosting** для frontend
- **CDN** для оптимизации

## 🚨 Устранение неполадок

### Если 404 ошибка:
1. Проверьте Environment Variables в Vercel
2. Убедитесь, что `vercel.json` настроен правильно
3. Проверьте правильность URL в `.env` файлах

### Если ошибка базы данных:
1. Запустите `python api/create_tables.py`
2. Проверьте доступность Supabase
3. Убедитесь в правильности DATABASE_URL

### Если ошибка сборки:
1. Проверьте `requirements.txt`
2. Убедитесь, что все зависимости корректны
3. Проверьте `.vercelignore` на исключения

## 🎉 Результат

После успешного развертывания у вас будет:
- **Полнофункциональная** образовательная платформа
- **Админ панель** для управления курсами
- **Система тестирования** с рандомизацией
- **Q&A система** для вопросов имаму
- **Команда проекта** с управлением
- **Responsive дизайн** для всех устройств

Платформа готова к использованию! 🚀