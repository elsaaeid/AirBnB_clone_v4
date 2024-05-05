$(document).ready( () => {
    const stateIds = {};
    const cityIds = {};
  
    // Listen to changes on each state input checkbox tag using arrow function
    $('.stateCheckBox').click(() => {
      if ($(this).prop('checked')) {
        stateIds[$(this).attr('data-id')] = $(this).attr('data-name');
      } else if (!$(this).prop('checked')) {
        delete stateIds[$(this).attr('data-id')];
      }
      updateLocationsH4();
    });
  
    // Listen to changes on each city input checkbox tag using arrow function
    $('.cityCheckBox').click(() => {
      if ($(this).prop('checked')) {
        cityIds[$(this).attr('data-id')] = $(this).attr('data-name');
      } else if (!$(this).prop('checked')) {
        delete cityIds[$(this).attr('data-id')];
      }
      updateLocationsH4();
    });
  
    // Function to update the h4 tag inside the div Locations with the list of States or Cities checked using arrow function
    const updateLocationsH4 = () => {
      if (Object.keys(stateIds).length === 0 && Object.keys(cityIds).length === 0) {
        $('.locations h4').html('&nbsp;');
      } else {
        $('.locations h4').text(Object.values(stateIds).concat(Object.values(cityIds)).join(', '));
      }
    };
  
    // Existing button click event listener for making a POST request to places_search using arrow function
    $('.filters button').click(() => {
      // Make the POST request with the list of Amenities, Cities, and States checked using arrow function
      $.ajax({
        type: 'POST',
        url: 'http://0.0.0.0:5001/api/v1/places_search/',
        contentType: 'application/json',
        data: JSON.stringify({
          amenities: Object.keys(amenityIds),
          states: Object.keys(stateIds),
          cities: Object.keys(cityIds)
        })
      }).done((data) => {
        // Update the section with the filtered places using arrow function
        $('section.places').empty();
        $('section.places').append('<h1>Places</h1>');
        for (const place of data) {
          // Create and append the template for each place using arrow function
          const template = `<article>
            <!-- Place information -->
          </article>`;
          $('section.places').append(template);
        }
      });
    });
  });
  