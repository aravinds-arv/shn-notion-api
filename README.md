# Slate

Tasks are powerful and important to track your progress. However, creating a task in a meeting, at your desk and on the go can take time and effort.<br>
Slate lets you create tasks quickly with a simple command line command directly into notion, without logging into your account. 🚀

## Adding Tasks
![demo](https://user-images.githubusercontent.com/78845005/170821250-bd6e1bb9-08b5-47d4-91be-0ac03f869121.gif)
<br>
<br>

## Notion Page
<img src="https://user-images.githubusercontent.com/78845005/170821281-6953809f-f4c6-4265-ba7a-e13e559f967b.gif" width=750>

## How to configure?
1. Create a new notion integration and copy token value
2. Duplicate the below notion page and copy the database ID
> _https://aravinds-arv.notion.site/TODO-5fd2ceaa5eaa4245ad63a810ca80b97c_
3. Copy config.py.sample to a new file config.py and replace the placeholders with your own interation token and database id
4. Install all requirements
```bash
   $ pip install -r requirements.txt
```
5. Finally run Slate 🎉

## Commands

Run without arguements to use voice commands 

```bash
  $ python slate.py
```

To add a new task to your notion database

```bash
   $ python slate.py add [TASK]
```

To remove an existing task from your notion database

```bash
  $ python slate.py remove [TASK_NUM]
```

To uncheck an existing task in your notion database

```bash
  $ python slate.py uncheck [TASK_NUM]
```

To list all existing unchecked tasks in your notion database

```bash
  $ python slate.py list
```

To open this help

```bash
   $ python slate.py help
```
