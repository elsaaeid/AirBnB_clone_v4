window.addEventListener('load', () => {
    // Existing tasks and event listeners
  
    // New feature: Show and hide reviews
    let reviewsVisible = false;
  
    // Event listener for the span next to the Reviews h2
    $('.reviews-toggle').click(() => {
      if (reviewsVisible) {
        // If the text is "hide", remove all Review elements from the DOM
        $('.review').remove();
        $('.reviews-toggle').text('show');
        reviewsVisible = false;
      } else {
        // If the text is "show", fetch, parse, and display reviews
        $.ajax({
          type: 'GET',
          url: 'http://0.0.0.0:5001/api/v1/reviews/',
          success: (data) => {
            // Display reviews
            for (const review of data) {
              // Create and append the template for each review
              const template = `
                <div class="review">
                  <h3>From ${review.user} the ${review.date}</h3>
                  <p>${review.text}</p>
                </div>`;
              $('.reviews').append(template);
            }
            $('.reviews-toggle').text('hide');
            reviewsVisible = true;
          }
        });
      }
    });
  });
  