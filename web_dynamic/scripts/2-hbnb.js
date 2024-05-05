$(document).ready(() => {
    const apiUrl = 'http://0.0.0.0:5001/api/v1/status/';
  
    $.get(apiUrl, (data) => {
      if (data.status === 'OK') {
        $('#api_status').addClass('available');
      } else {
        $('#api_status').removeClass('available');
      }
    });
  });
  