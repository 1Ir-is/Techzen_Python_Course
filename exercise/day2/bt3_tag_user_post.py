# Danh sách user: list tuple (user_id, name)
users = [
    ("U01", "Alice"),
    ("U02", "Bob"),
    ("U03", "Charlie"),
]

# Dict bài viết: key là post_id, value là dict thông tin
posts = {
    "P01": {
        "title": "Hoc Python co ban",
        "author_id": "U01",
        "tags": {"python", "beginner"},
    },
    "P02": {
        "title": "Lam viec voi List va Dict",
        "author_id": "U01",
        "tags": {"python", "data-structure"},
    },
    "P03": {
        "title": "Gioi thieu HTML CSS",
        "author_id": "U02",
        "tags": {"web", "frontend"},
    },
}

#Cau a: Tạo một dict `user_map` từ `users`, map `user_id` sang `name`
user_map = {}
for user_id, name in users:
    user_map[user_id] = name

#Cau b: Dùng vòng lặp duyệt `posts.items()` để in
for post_id, post in posts.items():
    title = post.get("title", "")
    author_id = post.get("author_id", "")
    author_name = user_map.get(author_id, "Unknown")
    tags = post.get("tags", set())
    tags_list = ", ".join(tags)
    print(f"[{post_id}] {title} - {author_name} - Tags: {tags_list}")


#Cau c: Tạo một set `all_tags` chứa toàn bộ tag xuất hiện trong mọi bài viết
all_tags = set()
for post in posts.values():
    all_tags.update(post.get("tags", set()))
print()
print(f"Tat ca cac tag: {all_tags}")
#     tags = post.get("tags", set())
#     for tag in tags:
#         all_tags.add(tag)
# print()
# print(f"All tags: {all_tags}")


#Cau d: Tạo một dict `tag_counter` để đếm số bài viết chứa mỗi tag
tag_counter = {}
for post in posts.values():
    for tag in post.get("tags", set()):
        tag_counter[tag] = tag_counter.get(tag, 0) + 1

print()
print("So bai viet moi tag:")
# for tag, count in tag_counter.items():
#     print(f"{tag}: {count}")

for tag in tag_counter:
    count = tag_counter[tag]
    print(f"{tag}: {count}")