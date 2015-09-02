angular.module('Falcon-email').factory('previewRenderSrvc', function ($http) {

	var html = ''

	return {
		render: function (data) {
			return $http({
				url: window.location,
				method: 'POST',
				transformRequest: function(obj) {
			        var str = [];
			        for(var p in obj)
			        str.push(encodeURIComponent(p) + "=" + encodeURIComponent(JSON.stringify(obj[p])));
			        return str.join("&");
			    },
				data: data,
				headers: {'Content-Type': 'application/json'},
			})
			.then(function (response) {
				return { html: response.data };
        	});
		}
	}	
});
