angular.module('Falcon-email').factory('previewRenderSrvc', function ($http) {

	var html = ''
	
	return {
		render: function (data) {
			return $http({
				url: window.location,
				method: 'POST',
				data: {
					data: data
				},
				headers: {'Content-Type': 'application/json'},
			})
			.then(function (response) {
				return { html: response.data };
        	});
		}
	}	
});
