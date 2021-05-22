// This is the script that will fetch and display the counter.
// window.addEventListener('DOMContentLoaded', (event) => {
//     getVisitCount();
// });


const functionApi = 'https://visitorcounter.azurewebsites.net/api/GetCounter?code=4mYCr1McGHA4t0ls8MjUCvJ8svXjJvZoaiOuwzJzTssIsHIA1jUbvw=='; 

const getVisitCount = () => {
    let count = 30;
    fetch(functionApi)
    .then(response => {
        return response.text()
    })
    .then(response => {
        console.log("Website called function API.",response);
        count = response;
        document.getElementById('counter').innerText = count;
    }).catch(function(error) {
        console.log(error);
      });
    return count;
}

getVisitCount();