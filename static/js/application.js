angular.module('Falcon-email', [])
	.controller('app', function ($scope, previewRenderSrvc){

		$scope.html = {}

		previewRenderSrvc.render({
 			'subject': 'lars'
 		}).then(function (data) {
 			$scope.render = data.html;
 		});


	});