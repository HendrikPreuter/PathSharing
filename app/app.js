angular.module("myApp", []).controller("myController", function($scope, $http) {
    httpRequest('');

    $scope.request = function (verb) {
        httpRequest(verb)
    };

    function httpRequest(verb) {
        $http({
            method: 'GET',
            url: 'http://localhost:5000/' + verb
        }).then(function successCallback(response) {
            $scope.jsVar = response.data;
        }, function errorCallback(response) {
            console.log(response);
        })
    }
});