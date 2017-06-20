angular.module("myApp", []).controller("myController", function($scope, $http) {
    $http({
        method: 'GET',
        url: 'http://localhost:5000/'
    }).then(function successCallback(response) {
        $scope.jsVar = response.data;
    }, function errorCallback(response) {
        console.log(response);
    });

    $scope.request = function(param){
        $http({
            method: 'GET',
            url: 'http://localhost:5000/' + param
        }).then(function successCallback(response) {
            $scope.jsVar = response.data;
        }, function errorCallback(response) {
            console.log(response);
        })};
});