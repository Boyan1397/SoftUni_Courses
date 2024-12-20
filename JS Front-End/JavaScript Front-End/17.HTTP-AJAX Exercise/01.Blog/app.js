function attachEvents() {
    
    // Posts - http://localhost:3030/jsonstore/blog/posts
    // Comments - http://localhost:3030/jsonstore/blog/comments
    
    const baseUrl = 'http://localhost:3030/jsonstore/blog';

    const selectPosts = document.querySelector('#posts');

    const postTitleEl = document.querySelector('#post-title');
    const postBodyEl = document.querySelector('#post-body');
    const postCommentsEl = document.querySelector('#post-comments');

    document.querySelector('#btnLoadPosts').addEventListener('click', loadHandler);
    document.querySelector('#btnViewPost').addEventListener('click', viewHandler);

    function loadHandler(e) {

        selectPosts.innerHTML = '';

        fetch(baseUrl + '/posts')
            .then(response => response.json())
            .then(posts => {
                
                Object.values(posts).forEach(post => {

                    const optionEl = document.createElement('option');

                    Object.assign(optionEl.dataset, post);

                    optionEl.textContent = post.title;
                    selectPosts.append( optionEl );
                });

            })
            .catch(error => console.error('Error: ', error));

    }

    function viewHandler(e) {

        fetch(baseUrl + '/comments')
        .then(response => response.json())
        .then(comments => {
            
            console.log(comments);

            const optionEl = selectPosts.querySelector('option:checked');

            postTitleEl.textContent = optionEl.dataset.title;
            postBodyEl.textContent = optionEl.dataset.body;
            
            Object.values(comments).forEach(comment => {
                if ( comment.postId === optionEl.dataset.id ) {
                    const commentEl = document.createElement('li');
                    commentEl.textContent = comment.text;
                    postCommentsEl.append( commentEl )    
                }
            });

        })
        .catch(error => console.error('Error: ', error));

    }

}

attachEvents();



// function attachEvents() {
//     const postsURL = 'http://localhost:3030/jsonstore/blog/posts'
//     const commentsURL = 'http://localhost:3030/jsonstore/blog/comments'

//     let loadPostsButton = document.getElementById('btnLoadPosts')
//     loadPostsButton.addEventListener('click', loadPostsEvent)

//     let postsSelect = document.getElementById('posts')

//     let viewPostButton = document.getElementById('btnViewPost')
//     viewPostButton.addEventListener('click', viewPostEvent)

//     allPosts = {}

//     async function loadPostsEvent(event) {
//         postsSelect.innerHTML = ''
//         let allPostsResponse = await fetch(postsURL)
//         allPosts = await allPostsResponse.json()
        
//         for (let postArr of Object.entries(allPosts)) {
//             let option = document.createElement('option')
//             option.textContent = postArr[1].title
//             option.value = postArr[0]
//             postsSelect.appendChild(option)
//         }
//     }

//     async function viewPostEvent(event) {
//         let currentPostObject = document.getElementById('posts')
//         let currentPostComments = []

//         let allCommentsResponse = await fetch(commentsURL)
//         let allComments = await allCommentsResponse.json()
        
//         for (let commentArr of Object.entries(allComments)) {
//             if (commentArr[1].postId === currentPostObject.value) {
//                 currentPostComments.push(commentArr[1].text)
//             }
//         }

//         let chosenPost = allPosts[currentPostObject.value]
    
//         let titleElement = document.getElementById('post-title')
//         titleElement.textContent = chosenPost.title

//         let postContentElement = document.getElementById('post-body')
//         postContentElement.textContent = chosenPost.body

//         let ul = document.getElementById('post-comments')
//         ul.innerHTML = ''
//         for (let comment of currentPostComments) {
//             let li = document.createElement('li')
//             li.textContent = comment
//             ul.appendChild(li)
//         }
//     }
// }

// attachEvents();