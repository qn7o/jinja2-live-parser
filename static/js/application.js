angular.module('Falcon-email', [])
	.controller('app', function ($scope, previewRenderSrvc){

		$scope.html = {}

		$scope.updateRender = function (value) {
			previewRenderSrvc.render(value).then(function (data) {
 				$scope.render = data.html;
 			});
		}
		
		//Initialize the template with no data.
		$scope.updateRender({})
	});