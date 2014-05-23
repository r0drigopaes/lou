var cohyControllers = angular.module('cohyControllers', []);

cohyControllers.controller('StationListCtrl', ['$scope', '$http',
    function ($scope, $http) {
        $scope.station_list = [];
        $http.get('/cohy/stations').success(function (data) {
            $scope.station_list = data

        });
    }]);

cohyControllers.controller('HomeCtrl', ['$translate','$scope',
    function ($translate, $scope) {
        $scope.changeLanguage = function(lang_key){
            $translate.use(lang_key);
        };
    }]);
