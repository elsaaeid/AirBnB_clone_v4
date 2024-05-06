$(document).ready(() => {
    const apiUrl = 'http://0.0.0.0:5001/api/v1/places_search/';
  
    $('button').click(() => {
      const amenities = [];
  
      $('input[type="checkbox"]:checked').each(function() {
        amenities.push($(this).data('id'));
      });
  
      const requestData = {
        amenities: amenities
      };
  
      $.ajax({
        url: apiUrl,
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(requestData),
        success: (data) => {
          $('.places').empty();
          data.forEach((place) => {
            const article = $('<article>');
            const title = $('<div>').addClass('title').text(place.name);
            const price = $('<div>').addClass('price_by_night').text(`$${place.price_by_night}`);
            const info = $('<div>').addClass('information');
            const maxGuests = $('<div>').addClass('max_guest').text(`${place.max_guest} Guest${place.max_guest !== 1 ? 's' : ''}`);
            const numberRooms = $('<div>').addClass('number_rooms').text(`${place.number_rooms} Bedroom${place.number_rooms !== 1 ? 's' : ''}`);
            const numberBathrooms = $('<div>').addClass('number_bathrooms').text(`${place.number_bathrooms} Bathroom${place.number_bathrooms !== 1 ? 's' : ''}`);
            const description = $('<div>').addClass('description').text(place.description);
  
            info.append(maxGuests, numberRooms, numberBathrooms);
            article.append(title, price, info, description);
            $('.places').append(article);
          });
        }
      });
    });
  });
