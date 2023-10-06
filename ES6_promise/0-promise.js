/* eslint-disable */
function getResponseFromAPI() {
    return new Promise((resolve, reject) => {
      if (resolve) {
        resolve('Work');
      } else {
        reject(Error('Broke'));
      }
    });
  }
  
  export default getResponseFromAPI;
      
