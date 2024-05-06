$(document).ready(() => {
    const amenities = {};
  
    $('input[type="checkbox"]').change(function() {
      const amenityId = $(this).data('id');
      const amenityName = $(this).data('name');
  
      if ($(this).is(':checked')) {
        amenities[amenityId] = amenityName;
      } else {
        delete amenities[amenityId];
      }
  
      const amenityList = Object.values(amenities).join(', ');
      $('.Amenities h4').text(`Amenities: ${amenityList}`);
    });
  });
  