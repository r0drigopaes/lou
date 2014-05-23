cohyApp.config(['$translateProvider', function ($translateProvider) {
    $translateProvider.translations('en_US', {
        'stations': 'Stations',
        'modules': 'Modules',
        'about': 'About',
        'contact': 'Contact',
        'cohy.description' : 'COHY stands for Computational Hydrology.',
        'learn.more' : 'Learn more',
        'station.list' : 'Station list',
        'new' : 'New',
        'choose.language' : 'Choose your language',
        'lang.pt_BR' : 'Portuguese',
        'lang.en_US' : 'English'
    });

    $translateProvider.translations('pt_BR', {
        'stations': 'Estações',
        'modules': 'Módulos',
        'about': 'Sobre',
        'contact': 'Contato',
        'cohy.description' : 'COHY é uma plataforma de Hidrologia Computacional.',
        'learn.more' : 'Saiba mais',
        'station.list' : 'Lista de estações',
        'new' : 'Nova',
        'choose.language' : 'Escolha sua linguagem',
        'lang.pt_BR' : 'Português',
        'lang.en_US' : 'Inglês'
    });

    $translateProvider.determinePreferredLanguage();
    //$translateProvider.preferredLanguage('en_US');
}]);
