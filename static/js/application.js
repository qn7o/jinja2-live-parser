angular.module('Falcon-email', [])
	.controller('app', function ($scope, previewRenderSrvc){

		$scope.html = {}

		$scope.updateRender = function (value) {
			previewRenderSrvc.render(value).then(function (data) {
 				$scope.render = data.html;
 			});
		}
		
		$scope.updateRender({})


	});