angular.module("myApp.login", []).controller("loginController", ['$scope', '$http', '$location', function($scope, $http, $location) {
    $scope.token = localStorage.getItem('token');
    if($scope.token !== null) {
        $http.defaults.header.common.Token = $scope.token;
        $location.path('../index.html');
    }

    $scope.login = function(user) {
        console.log('logging in.');
        var data = {
            'username': user.username,
            'password': user.password
        };
        console.log(data);
        $http.post("http://localhost:5000/login", data).then(function (response) {
            if(response.data.response === 'error') {
                console.log('Error')
            }

            else {
                console.log('Logged in');
                alert("Logged in");
                $scope.token = response.data.token;
                $http.defaults.headers.common.Token = $scope.token;
                window.location.href = '../../index.html';
            }
        })
    }
}]);