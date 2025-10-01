# Blog Post Management Features

## Features
- Users can create, read, update, and delete blog posts.
- Only authenticated users can create posts.
- Only post authors can edit or delete their own posts.
- All visitors can view the list of posts and details.

## URLs
- `/posts/` → List all posts
- `/posts/new/` → Create a new post (login required)
- `/posts/<id>/` → View post details
- `/posts/<id>/edit/` → Edit post (author only)
- `/posts/<id>/delete/` → Delete post (author only)

## Testing
1. Register/login as a user.
2. Create new posts.
3. Edit/delete only your own posts.
4. Logout and check that create/edit/delete are restricted.
