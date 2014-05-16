cohyApp.config(['$routeProvider','urls',
    function($routeProvider,urls){
        $routeProvider.
            when('/stations', {
                templateUrl : urls.partial_stations,
                controller : 'StationListCtrl'
            }).
            when('/home', {
                templateUrl : urls.partial_home,
                controller : 'HomeCtrl'
            }).
            otherwise({
                redirectTo: '/home'
            });
    }
]);

cohyApp.config(function($httpProvider) {
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
});
