import json
import os
import sys


def zip_file2(dir, file_news):
    sh = 'zip -r ' + file_news + " " + dir
    print(sh)
    print(os.popen(sh))


def findZippedProject():
    baseProject = '/home/fdse/sbw/maven500/'
    projectList = os.listdir(baseProject)
    zip = []
    for projectDir in projectList:
        list = os.listdir(baseProject + projectDir)
        zip.extend(list)
    return zip


def findLocalZippedProject():
    baseProject = 'd:/maven500/'
    return os.listdir(baseProject)


if __name__ == '__main__':
    local = '["AdoptOpenJDK__fdse__jitwatch.zip", "advantageous__fdse__qbit.zip", "afollestad__fdse__ason.zip", "afollestad__fdse__bridge.zip", "airbnb__fdse__aerosolve.zip", "airbnb__fdse__airpal.zip", "ajermakovics__fdse__jvm-mon.zip", "albertlatacz__fdse__java-repl.zip", "andsel__fdse__moquette.zip", "aNNiMON__fdse__Lightweight-Stream-API.zip", "aol__fdse__cyclops-react.zip", "aol__fdse__micro-server.zip", "apache__fdse__aurora.zip", "apache__fdse__beam.zip", "apache__fdse__geode.zip", "apache__fdse__groovy.zip", "apache__fdse__kafka.zip", "apache__fdse__ofbiz.zip", "apereo__fdse__cas.zip", "AppliedEnergistics__fdse__Applied-Energistics-2.zip", "AsamK__fdse__signal-cli.zip", "auth0__fdse__java-jwt.zip", "azkaban__fdse__azkaban.zip", "bcgit__fdse__bc-java.zip", "ben-manes__fdse__caffeine.zip", "bennidi__fdse__mbassador.zip", "bitcoinj__fdse__bitcoinj.zip", "btraceio__fdse__btrace.zip", "BuildCraft__fdse__BuildCraft.zip", "cbeust__fdse__jcommander.zip", "cbeust__fdse__testng.zip", "centic9__fdse__jgit-cookbook.zip", "ChrisRM__fdse__material-theme-jetbrains.zip", "cloudfoundry__fdse__uaa.zip", "cmusphinx__fdse__sphinx4.zip", "codeborne__fdse__selenide.zip", "codebutler__fdse__android-websockets.zip", "crate__fdse__crate.zip", "dboissier__fdse__mongo4idea.zip", "dcendents__fdse__android-maven-gradle-plugin.zip", "dcevm__fdse__dcevm.zip", "dreamhead__fdse__moco.zip", "drewnoakes__fdse__metadata-extractor.zip", "DV8FromTheWorld__fdse__JDA.zip", "ehcache__fdse__ehcache3.zip", "elastic__fdse__elasticsearch-hadoop.zip", "elastic__fdse__elasticsearch.zip", "embulk__fdse__embulk.zip", "encog__fdse__encog-java-core.zip", "EnterpriseQualityCoding__fdse__FizzBuzzEnterpriseEdition.zip", "ethereum__fdse__ethereumj.zip", "fesh0r__fdse__fernflower.zip", "functionaljava__fdse__functionaljava.zip", "go-lang-plugin-org__fdse__go-lang-idea-plugin.zip", "gocd__fdse__gocd.zip", "googlemaps__fdse__google-maps-services-java.zip", "google__fdse__binnavi.zip", "google__fdse__re2j.zip", "grails__fdse__grails-core.zip", "graphql-java__fdse__graphql-java.zip", "groovy__fdse__groovy-core.zip", "Grover-c13__fdse__PokeGOAPI-Java.zip", "h2oai__fdse__h2o-3.zip", "Haehnchen__fdse__idea-php-symfony2-plugin.zip", "hamcrest__fdse__JavaHamcrest.zip", "hibernate__fdse__hibernate-orm.zip", "hierynomus__fdse__sshj.zip", "hsz__fdse__idea-gitignore.zip", "huanghongxun__fdse__HMCL.zip", "i2p__fdse__i2p.i2p.zip", "ignatov__fdse__intellij-erlang.zip", "igniterealtime__fdse__Smack.zip", "JabRef__fdse__jabref.zip", "jankotek__fdse__mapdb.zip", "java-json-tools__fdse__json-schema-validator.zip", "jbake-org__fdse__jbake.zip", "jcoleman__fdse__tomcat-redis-session-manager.zip", "JesusFreke__fdse__smali.zip", "JetBrains__fdse__ideavim.zip", "jfoenixadmin__fdse__JFoenix.zip", "jhusain__fdse__learnrxjava.zip", "jprante__fdse__elasticsearch-jdbc.zip", "json-path__fdse__JsonPath.zip", "junit-team__fdse__junit5.zip", "kevin-wayne__fdse__algs4.zip", "konifar__fdse__android-material-design-icon-generator-plugin.zip", "KronicDeth__fdse__intellij-elixir.zip", "lenskit__fdse__lenskit.zip", "leventov__fdse__Koloboke.zip", "libgdx__fdse__ashley.zip", "libgdx__fdse__gdx-ai.zip", "liferay__fdse__liferay-plugins.zip", "line__fdse__armeria.zip", "linkedin__fdse__ambry.zip", "linkedin__fdse__cleo.zip", "linkedin__fdse__cruise-control.zip", "linkedin__fdse__databus.zip", "linkedin__fdse__FeatureFu.zip", "linkedin__fdse__flashback.zip", "linkedin__fdse__kafka-monitor.zip", "linkedin__fdse__PalDB.zip", "linkedin__fdse__rest.li.zip", "linkedin__fdse__WhereHows.zip", "LMAX-Exchange__fdse__disruptor.zip", "LogNet__fdse__grpc-spring-boot-starter.zip", "mahmoudparsian__fdse__data-algorithms-book.zip", "methusalah__fdse__OpenRTS.zip", "micrometer-metrics__fdse__micrometer.zip", "mihaip__fdse__dex-method-counts.zip", "MinecraftForge__fdse__MinecraftForge.zip", "mission-peace__fdse__interview.zip", "mockito__fdse__mockito.zip", "mongodb__fdse__mongo-hadoop.zip", "mongodb__fdse__mongo-java-driver.zip", "mongodb__fdse__morphia.zip", "MovingBlocks__fdse__Terasology.zip", "mplushnikov__fdse__lombok-intellij-plugin.zip", "NanoHttpd__fdse__nanohttpd.zip", "nelenkov__fdse__android-backup-extractor.zip", "neo4j-contrib__fdse__neo4j-apoc-procedures.zip", "Netflix__fdse__archaius.zip", "Netflix__fdse__astyanax.zip", "Netflix__fdse__blitz4j.zip", "Netflix__fdse__eureka.zip", "Netflix__fdse__EVCache.zip", "Netflix__fdse__Fenzo.zip", "Netflix__fdse__genie.zip", "Netflix__fdse__governator.zip", "Netflix__fdse__hollow.zip", "Netflix__fdse__Hystrix.zip", "Netflix__fdse__Priam.zip", "Netflix__fdse__ribbon.zip", "Netflix__fdse__servo.zip", "Netflix__fdse__SimianArmy.zip", "Netflix__fdse__suro.zip", "Netflix__fdse__Turbine.zip", "Netflix__fdse__zuul.zip", "oblac__fdse__jodd.zip", "p6spy__fdse__p6spy.zip", "pahimar__fdse__Equivalent-Exchange-3.zip", "palantir__fdse__atlasdb.zip", "paulc4__fdse__microservices-demo.zip", "pbreault__fdse__adb-idea.zip", "pedrovgs__fdse__AndroidWiFiADB.zip", "powermock__fdse__powermock.zip", "puniverse__fdse__quasar.zip", "pxb1988__fdse__dex2jar.zip", "Raysmond__fdse__SpringBlog.zip", "reactive-streams__fdse__reactive-streams-jvm.zip", "ReactiveX__fdse__RxJava.zip", "ReactiveX__fdse__RxNetty.zip", "reactor__fdse__reactor-core.zip", "real-logic__fdse__aeron.zip", "real-logic__fdse__agrona.zip", "real-logic__fdse__simple-binary-encoding.zip", "resilience4j__fdse__resilience4j.zip", "rharter__fdse__auto-value-gson.zip", "rharter__fdse__auto-value-parcel.zip", "rholder__fdse__guava-retrying.zip", "royclarkson__fdse__spring-rest-service-oauth.zip", "RuedigerMoeller__fdse__fast-serialization.zip", "sgroschupf__fdse__zkclient.zip", "shekhargulati__fdse__strman-java.zip", "Sixt__fdse__ja-micro.zip", "sk89q__fdse__WorldEdit.zip", "skylot__fdse__jadx.zip", "sleekbyte__fdse__tailor.zip", "SlimeKnights__fdse__TinkersConstruct.zip", "SonarSource__fdse__sonarqube.zip", "spockframework__fdse__spock.zip", "SpongePowered__fdse__SpongeAPI.zip", "SpongePowered__fdse__SpongeForge.zip", "spring-io__fdse__sagan.zip", "spring-projects__fdse__spring-batch.zip", "spring-projects__fdse__spring-framework.zip", "spring-projects__fdse__spring-hadoop.zip", "spring-projects__fdse__spring-integration-samples.zip", "spring-projects__fdse__spring-integration.zip", "spring-projects__fdse__spring-loaded.zip", "spring-projects__fdse__spring-restdocs.zip", "spring-projects__fdse__spring-security.zip", "spring-projects__fdse__spring-session.zip", "spring-projects__fdse__spring-social.zip", "square__fdse__okio.zip", "square__fdse__tape.zip", "stagemonitor__fdse__stagemonitor.zip", "stanfordnlp__fdse__CoreNLP.zip", "Swagger2Markup__fdse__swagger2markup.zip", "syncany__fdse__syncany.zip", "testcontainers__fdse__testcontainers-java.zip", "tomakehurst__fdse__wiremock.zip", "treasure-data__fdse__digdag.zip", "unclebob__fdse__fitnesse.zip", "UnderwaterApps__fdse__overlap2d.zip", "VaughnVernon__fdse__IDDD_Samples.zip", "Vazkii__fdse__Botania.zip", "voldemort__fdse__voldemort.zip", "web3j__fdse__web3j.zip", "winterDroid__fdse__android-drawable-importer-intellij-plugin.zip", "wiztools__fdse__rest-client.zip", "yidongnan__fdse__spring-cloud-netflix-example.zip", "YiiGuxing__fdse__TranslationPlugin.zip", "zzz40500__fdse__GsonFormat.zip"]'
    list = json.loads(local)
    # zipped project
    zippedProject = findZippedProject()
    zippedProject.extend(list)
    print(len(list))
    # localProjects = findLocalZippedProject()

    # java 500+ project
    f = open('java500.txt')
    content = f.read()
    javaProjectList = json.loads(content)
    f.close()

    # zip files
    index = sys.argv[1]
    index = int(index)
    cnt = 0
    max = 20
    for javaProject in javaProjectList:
        isMaven = javaProject['maven']
        isAndroid = javaProject['android']
        if isMaven and not isAndroid:
            # is Maven but not android
            proj = javaProject['proj']
            companyName = proj.split('/')[-2]
            projectName = proj.split('/')[-1]
            fileName = companyName + '__fdse__' + projectName + '.zip'
            if fileName in zippedProject:
                print('in')
                continue
            else:
                dest = 'maven500/' + str(index) + '/'
                if not os.path.exists(dest):
                    os.makedirs(dest)
                zip_file2(proj, dest + fileName)
                cnt += 1
                if cnt >= max:
                    cnt = 0
                    index += 1
