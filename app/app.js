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
            // $scope.jsVar = response.data;
            $scope.jsVar = [1, 2, 3, 4, 5];
        }, function errorCallback(response) {
            console.log(response);
        })
    }
});