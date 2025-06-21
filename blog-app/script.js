const API_URL = "http://localhost:5000/posts";

// Fetch and display posts when the page loads
document.addEventListener("DOMContentLoaded", fetchPosts);

// Handle form submission
document.getElementById("postForm").addEventListener("submit", function (event) {
    event.preventDefault();
    const title = document.getElementById("title").value;
    const content = document.getElementById("content").value;

    if (!title || !content) {
        alert("Please fill in both fields");
        return;
    }

    // Send POST request to add new post
    fetch(API_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ title, content }),
    })
        .then((response) => {
            if (!response.ok) {
                throw new Error("Failed to add post");
            }
            return response.json();
        })
        .then(() => {
            document.getElementById("postForm").reset();
            fetchPosts(); // Refresh posts
        })
        .catch((error) => {
            console.error("Error:", error);
        });
});

// Fetch posts and display them
function fetchPosts() {
    fetch(API_URL)
        .then((response) => response.json())
        .then((posts) => {
            const postsContainer = document.getElementById("posts");
            postsContainer.innerHTML = "";
            posts.forEach((post) => {
                const postElement = document.createElement("div");
                postElement.className = "post";
                postElement.innerHTML = `
                    <h3>${post.title}</h3>
                    <p>${post.content}</p>
                    <button onclick="deletePost(${post.id})">Delete</button>
                `;
                postsContainer.appendChild(postElement);
            });
        })
        .catch((error) => {
            console.error("Error fetching posts:", error);
        });
}

// Delete a post by ID
function deletePost(id) {
    fetch(`${API_URL}/${id}`, {
        method: "DELETE",
    })
        .then((response) => {
            if (!response.ok) {
                throw new Error("Failed to delete post");
            }
            return response.json();
        })
        .then(() => {
            fetchPosts(); // Refresh posts after deletion
        })
        .catch((error) => {
            console.error("Error deleting post:", error);
        });
}
