<!-- changelog is partially generated, so it doesn't follow headings and required structure, so we disable it. -->
<!-- markdownlint-disable -->

<a name="unreleased"></a>
# Unreleased

## Bug Fixes

* removed ambiguous quotes from labels.
* sight, yes a whitespace character breaks the build
* typo in input for layer workflow
* no need to cache npm since we only install cdk cli and don't have .lock files
* add entire ARN role instead of account and role name
* use addHandler over monkeypatch
* mathc the name of the cdk synth from the build phase
* repurpose test to cover parent loggers case
* package_logger as const over logger instance
* path to artefact
* mypy errors
* unzip the right artifact name
* parallel_run should fail when e2e tests fail
* bump aws-cdk version
* git-chlg docker image is broken
* download artefact into the layer dir
* lock dependencies
* lint files
* **api_gateway:** fixed custom metrics issue when using debug mode ([#1827](https://github.com/awslabs/aws-lambda-powertools-python/issues/1827))
* **api_gateway:** allow whitespace in routes' path parameter ([#1099](https://github.com/awslabs/aws-lambda-powertools-python/issues/1099))
* **api_gateway:** allow whitespace in routes' path parameter ([#1099](https://github.com/awslabs/aws-lambda-powertools-python/issues/1099))
* **apigateway:** support dynamic routes with equal sign (RFC3986) ([#1737](https://github.com/awslabs/aws-lambda-powertools-python/issues/1737))
* **apigateway:** update Response class to require status_code only ([#1560](https://github.com/awslabs/aws-lambda-powertools-python/issues/1560))
* **apigateway:** remove indentation in debug_mode ([#987](https://github.com/awslabs/aws-lambda-powertools-python/issues/987))
* **apigateway:** support nested router decorators ([#1709](https://github.com/awslabs/aws-lambda-powertools-python/issues/1709))
* **batch:** docstring fix for success_handler() record parameter ([#1202](https://github.com/awslabs/aws-lambda-powertools-python/issues/1202))
* **batch:** delete >10 messages in legacy sqs processor ([#818](https://github.com/awslabs/aws-lambda-powertools-python/issues/818))
* **batch:** missing space in BatchProcessingError message ([#1201](https://github.com/awslabs/aws-lambda-powertools-python/issues/1201))
* **batch:** bugfix to clear exceptions between executions ([#1022](https://github.com/awslabs/aws-lambda-powertools-python/issues/1022))
* **ci:** only run e2e tests on py 3.7
* **ci:** use docker driver on buildx
* **ci:** build without buildkit
* **ci:** fix arm64 layer builds
* **ci:** remove v2 suffix from SAR apps ([#1633](https://github.com/awslabs/aws-lambda-powertools-python/issues/1633))
* **ci:** new artifact path, sed gnu/linux syntax, and pypi test
* **ci:** temporarly remove pypi test deployment
* **ci:** secret and OIDC inheritance in nested children workflow
* **ci:** quote prBody GH expr on_opened_pr
* **ci:** upgraded cdk to match the version used on e2e tests
* **ci:** remove utf-8 body in octokit body req
* **ci:** workflow should use npx for CDK CLI
* **ci:** disable merged_pr workflow
* **ci:** improve msg visibility on closed issues
* **ci:** integrate isort 5.0 with black to resolve conflicts
* **ci:** linting issues after flake8-blackbear,mypy upgrades
* **ci:** checkout project before validating related issue workflow
* **ci:** regex to catch combination of related issues workflow
* **ci:** reusable workflow secrets param
* **ci:** regex to catch combination of related issues workflow
* **ci:** ignore v2 action for now
* **ci:** setup git client earlier to prevent dirty stash error
* **ci:** disable pre-commit hook download from version bump
* **ci:** pass core fns to large pr workflow script
* **ci:** on_label permissioning model & workflow execution
* **ci:** ensure PR_AUTHOR is present for large_pr_split workflow
* **ci:** gracefully and successful exit changelog upon no changes
* **ci:** event resolution for on_label_added workflow
* **ci:** calculate parallel jobs based on infrastructure needs ([#1475](https://github.com/awslabs/aws-lambda-powertools-python/issues/1475))
* **ci:** del flake8 direct dep over py3.6 conflicts and docs failure
* **ci:** label_related_issue unresolved var from history mixup
* **ci:** move from pip-tools to poetry on layers to fix conflicts
* **ci:** typo and bust gh actions cache
* **ci:** use poetry to resolve layer deps; pip for CDK
* **ci:** disable poetry venv for layer workflow as cdk ignores venv
* **ci:** add cdk v2 dep for layers workflow
* **ci:** move from pip-tools to poetry on layers reusable workflow
* **ci:** move from pip-tools to poetry on layers
* **ci:** temporarily disable changelog upon release
* **ci:** add explicit origin to fix release detached head
* **ci:** increase permission to allow version sync back to repo
* **ci:** changelog workflow must receive git tags too
* **ci:** add additional input to accurately describe intent on skip
* **ci:** job permissions
* **ci:** api docs path
* **ci:** add missing oidc token generation permission
* **ci:** use gh-pages env as official docs are wrong
* **ci:** allow inherit secrets for reusable workflow
* **ci:** remove unused secret
* **ci:** scope e2e tests by python version
* **ci:** cond doesnt support two expr w/ env
* **ci:** only event is resolved in cond
* **ci:** remove unsupported env in workflow_call
* **ci:** unexpected symbol due to double quotes...
* **ci:** add auth to API HTTP Gateway and Lambda Function Url ([#1882](https://github.com/awslabs/aws-lambda-powertools-python/issues/1882))
* **ci:** keep layer version permission ([#1318](https://github.com/awslabs/aws-lambda-powertools-python/issues/1318))
* **ci:** lambda layer workflow release version and conditionals ([#1316](https://github.com/awslabs/aws-lambda-powertools-python/issues/1316))
* **ci:** fetch all git info so we can check tags
* **ci:** lambda layer workflow release version and conditionals ([#1316](https://github.com/awslabs/aws-lambda-powertools-python/issues/1316))
* **ci:** remove additional quotes in PR action ([#1317](https://github.com/awslabs/aws-lambda-powertools-python/issues/1317))
* **ci:** install poetry before calling setup/python with cache ([#1315](https://github.com/awslabs/aws-lambda-powertools-python/issues/1315))
* **ci:** pr label regex for special chars in title
* **ci:** fixes typos and small issues on github scripts ([#1302](https://github.com/awslabs/aws-lambda-powertools-python/issues/1302))
* **ci:** address conditional type on_merge
* **ci:** address pr title semantic not found logic
* **ci:** address gh-actions additional quotes; remove debug
* **ci:** regex group name for on_merge workflow
* **ci:** escape outputs as certain PRs can break GH Actions expressions
* **ci:** checkout project before validating related issue workflow
* **ci:** move conditionals from yaml to code
* **ci:** accept core arg in label related issue workflow
* **ci:** match the name of the cdk synth from the build phase
* **ci:** move conditionals from yaml to code; leftover
* **ci:** merged_pr add issues write access
* **core:** fixes leftovers from rebase
* **data-classes:** Add missing SES fields and ([#1045](https://github.com/awslabs/aws-lambda-powertools-python/issues/1045))
* **deps:** bump dev dep mako version to address CVE-2022-40023 ([#1524](https://github.com/awslabs/aws-lambda-powertools-python/issues/1524))
* **deps:** update jmespath marker to support 1.0 and py3.6 ([#1139](https://github.com/awslabs/aws-lambda-powertools-python/issues/1139))
* **deps:** correct mypy types as dev dependency ([#1322](https://github.com/awslabs/aws-lambda-powertools-python/issues/1322))
* **deps:** Ignore boto3 changes until needed ([#1151](https://github.com/awslabs/aws-lambda-powertools-python/issues/1151))
* **deps:** correct py36 marker for jmespath
* **deps:** update build system to poetry-core ([#1651](https://github.com/awslabs/aws-lambda-powertools-python/issues/1651))
* **deps-dev:** remove jmespath due to dev deps conflict  ([#1148](https://github.com/awslabs/aws-lambda-powertools-python/issues/1148))
* **docs:** remove Slack link ([#1210](https://github.com/awslabs/aws-lambda-powertools-python/issues/1210))
* **event-handler:** body to empty string in CORS preflight (ALB non-compliant) ([#1249](https://github.com/awslabs/aws-lambda-powertools-python/issues/1249))
* **event_handler:** Allow for event_source support ([#1159](https://github.com/awslabs/aws-lambda-powertools-python/issues/1159))
* **event_handler:** docs snippets, high-level import CorsConfig ([#1019](https://github.com/awslabs/aws-lambda-powertools-python/issues/1019))
* **event_handler:** exception_handler to handle ServiceError exceptions ([#1160](https://github.com/awslabs/aws-lambda-powertools-python/issues/1160))
* **event_handlers:** handle lack of headers when using auto-compression feature ([#1325](https://github.com/awslabs/aws-lambda-powertools-python/issues/1325))
* **event_handlers:** ImportError when importing Response from top-level event_handler ([#1388](https://github.com/awslabs/aws-lambda-powertools-python/issues/1388))
* **event_handlers:** omit explicit None HTTP header values ([#1793](https://github.com/awslabs/aws-lambda-powertools-python/issues/1793))
* **event_sources:** implement Mapping protocol on DictWrapper for better interop with existing middlewares ([#1516](https://github.com/awslabs/aws-lambda-powertools-python/issues/1516))
* **event_sources:** add test for Function URL AuthZ ([#1421](https://github.com/awslabs/aws-lambda-powertools-python/issues/1421))
* **feature-flags:** revert RuleAction Enum inheritance on str ([#1910](https://github.com/awslabs/aws-lambda-powertools-python/issues/1910))
* **governance:** update label in names in issues
* **idempotency:** idempotent_function should support standalone falsy values ([#1669](https://github.com/awslabs/aws-lambda-powertools-python/issues/1669))
* **idempotency:** make idempotent_function decorator thread safe ([#1899](https://github.com/awslabs/aws-lambda-powertools-python/issues/1899))
* **idempotency:** pass by value on idem key to guard inadvert mutations ([#1090](https://github.com/awslabs/aws-lambda-powertools-python/issues/1090))
* **jmespath_util:** snappy as dev dep and typing example ([#1446](https://github.com/awslabs/aws-lambda-powertools-python/issues/1446))
* **lambda-authorizer:** allow proxy resources path in arn ([#1051](https://github.com/awslabs/aws-lambda-powertools-python/issues/1051))
* **license:** correction to MIT + MIT-0 (no proprietary anymore) ([#1883](https://github.com/awslabs/aws-lambda-powertools-python/issues/1883))
* **license:** add MIT-0 license header ([#1871](https://github.com/awslabs/aws-lambda-powertools-python/issues/1871))
* **logger:** support additional args for handlers when injecting lambda context ([#1276](https://github.com/awslabs/aws-lambda-powertools-python/issues/1276))
* **logger:** support exception and exception_name fields at any log level ([#1930](https://github.com/awslabs/aws-lambda-powertools-python/issues/1930))
* **logger:** fix unknown attributes being ignored by mypy ([#1670](https://github.com/awslabs/aws-lambda-powertools-python/issues/1670))
* **logger:** clear_state regression on absent standard keys ([#1088](https://github.com/awslabs/aws-lambda-powertools-python/issues/1088))
* **logger:** ensure state is cleared for custom formatters ([#1072](https://github.com/awslabs/aws-lambda-powertools-python/issues/1072))
* **logger:** test generates logfile
* **logger:** exclude source_logger in copy_config_to_registered_loggers ([#1001](https://github.com/awslabs/aws-lambda-powertools-python/issues/1001))
* **logger:** preserve std keys when using custom formatters ([#1264](https://github.com/awslabs/aws-lambda-powertools-python/issues/1264))
* **logger:** clear_state should keep custom key formats ([#1095](https://github.com/awslabs/aws-lambda-powertools-python/issues/1095))
* **logger:** preserve std keys when using custom formatters ([#1264](https://github.com/awslabs/aws-lambda-powertools-python/issues/1264))
* **logger-utils:** regression on exclude set leading to no formatter ([#1080](https://github.com/awslabs/aws-lambda-powertools-python/issues/1080))
* **metrics:** flush upon a single metric 100th data point ([#1046](https://github.com/awslabs/aws-lambda-powertools-python/issues/1046))
* **metrics:** clarify no-metrics user warning ([#1935](https://github.com/awslabs/aws-lambda-powertools-python/issues/1935))
* **metrics:** ensure dimension_set is reused across instances (pointer) ([#1581](https://github.com/awslabs/aws-lambda-powertools-python/issues/1581))
* **metrics:** raise SchemaValidationError for >8 metric dimensions ([#1240](https://github.com/awslabs/aws-lambda-powertools-python/issues/1240))
* **middleware_factory:** ret type annotation for handler dec ([#1066](https://github.com/awslabs/aws-lambda-powertools-python/issues/1066))
* **parameters:** get_secret correctly return SecretBinary value ([#1717](https://github.com/awslabs/aws-lambda-powertools-python/issues/1717))
* **parser:** Add missing fields for SESEvent ([#1027](https://github.com/awslabs/aws-lambda-powertools-python/issues/1027))
* **parser:** raise ValidationError when SNS->SQS keys are intentionally missing ([#1299](https://github.com/awslabs/aws-lambda-powertools-python/issues/1299))
* **parser:** loose validation on SNS fields to support FIFO ([#1606](https://github.com/awslabs/aws-lambda-powertools-python/issues/1606))
* **parser:** S3Model Object Deleted omits size and eTag attr ([#1638](https://github.com/awslabs/aws-lambda-powertools-python/issues/1638))
* **tests:** make logs fetching more robust ([#1878](https://github.com/awslabs/aws-lambda-powertools-python/issues/1878))
* **tests:** make sure multiple e2e tests run concurrently ([#1861](https://github.com/awslabs/aws-lambda-powertools-python/issues/1861))
* **tests:** remove custom workers
* **typing:** level arg in copy_config_to_registered_loggers ([#1534](https://github.com/awslabs/aws-lambda-powertools-python/issues/1534))
* **typing:** fix mypy error

## Code Refactoring

* rename to clear_state
* rename to remove_custom_keys
* **apigateway:** remove POWERTOOLS_EVENT_HANDLER_DEBUG env var ([#1620](https://github.com/awslabs/aws-lambda-powertools-python/issues/1620))
* **batch:** remove legacy sqs_batch_processor ([#1492](https://github.com/awslabs/aws-lambda-powertools-python/issues/1492))
* **e2e:** make table name dynamic
* **e2e:** fix idempotency typing

## Documentation

* fix syntax errors and line highlights ([#1004](https://github.com/awslabs/aws-lambda-powertools-python/issues/1004))
* add better BDD coments
* project name consistency
* fix anchor
* **apigateway:** add all resolvers in testing your code section for accuracy ([#1688](https://github.com/awslabs/aws-lambda-powertools-python/issues/1688))
* **apigateway:** removes duplicate admonition ([#1426](https://github.com/awslabs/aws-lambda-powertools-python/issues/1426))
* **appsync:** fix typo
* **batch:** document the new lambda context feature
* **batch:** remove legacy reference to sqs processor
* **community:** fix social handlers for Ran ([#1654](https://github.com/awslabs/aws-lambda-powertools-python/issues/1654))
* **community:** fix twitch parent domain for embedded video
* **contributing:** operational excellence pause
* **engine:** re-enable clipboard button for code snippets
* **event-handler:** snippets split, improved, and lint ([#1279](https://github.com/awslabs/aws-lambda-powertools-python/issues/1279))
* **event-handler:** snippets split, improved, and lint ([#1279](https://github.com/awslabs/aws-lambda-powertools-python/issues/1279))
* **event-handler:** improve testing section for graphql ([#996](https://github.com/awslabs/aws-lambda-powertools-python/issues/996))
* **event-source:**  fix incorrect method in example CloudWatch Logs ([#1857](https://github.com/awslabs/aws-lambda-powertools-python/issues/1857))
* **event_handlers:** Fix REST API - HTTP Methods documentation ([#1936](https://github.com/awslabs/aws-lambda-powertools-python/issues/1936))
* **examples:** linting unnecessary whitespace
* **examples:** enforce and fix all mypy errors ([#1393](https://github.com/awslabs/aws-lambda-powertools-python/issues/1393))
* **governance:** typos on PR template fixes [#1314](https://github.com/awslabs/aws-lambda-powertools-python/issues/1314)
* **governance:** add security doc to the root
* **governance:** new form to allow customers self-nominate as public reference ([#1589](https://github.com/awslabs/aws-lambda-powertools-python/issues/1589))
* **governance:** allow community to suggest feature content ([#1593](https://github.com/awslabs/aws-lambda-powertools-python/issues/1593))
* **governance:** link roadmap and maintainers doc
* **graphql:** snippets split, improved, and lint ([#1287](https://github.com/awslabs/aws-lambda-powertools-python/issues/1287))
* **home:** update powertools definition
* **home:** add discord invitation link ([#1471](https://github.com/awslabs/aws-lambda-powertools-python/issues/1471))
* **home:** fix discord syntax and add Discord badge
* **homepage:** note about v2 version
* **homepage:** add Pulumi code example ([#1652](https://github.com/awslabs/aws-lambda-powertools-python/issues/1652))
* **homepage:** remove 3.6 and add hero image
* **homepage:** remove v1 layer limitation on pydantic not being included
* **homepage:** introduce POWERTOOLS_DEV env var ([#1569](https://github.com/awslabs/aws-lambda-powertools-python/issues/1569))
* **homepage:** emphasize additional powertools languages ([#1292](https://github.com/awslabs/aws-lambda-powertools-python/issues/1292))
* **homepage:** include .NET powertools
* **homepage:** add banner for end-of-support v1 ([#1879](https://github.com/awslabs/aws-lambda-powertools-python/issues/1879))
* **homepage:** set url for end-of-support in announce block ([#1893](https://github.com/awslabs/aws-lambda-powertools-python/issues/1893))
* **homepage:** Replace poetry command to add group parameter ([#1917](https://github.com/awslabs/aws-lambda-powertools-python/issues/1917))
* **homepage:** auto-update Layer ARN on every release ([#1610](https://github.com/awslabs/aws-lambda-powertools-python/issues/1610))
* **homepage:** update default value for `POWERTOOLS_DEV` ([#1695](https://github.com/awslabs/aws-lambda-powertools-python/issues/1695))
* **idempotency:** add missing Lambda Context; note on thread-safe ([#1732](https://github.com/awslabs/aws-lambda-powertools-python/issues/1732))
* **idempotency:** "persisntence" typo ([#1596](https://github.com/awslabs/aws-lambda-powertools-python/issues/1596))
* **idempotency:** fix register_lambda_context order ([#1747](https://github.com/awslabs/aws-lambda-powertools-python/issues/1747))
* **idempotency:** fix, improve, and increase visibility for batch integration ([#1776](https://github.com/awslabs/aws-lambda-powertools-python/issues/1776))
* **idempotency:** add IAM permissions section ([#1902](https://github.com/awslabs/aws-lambda-powertools-python/issues/1902))
* **index:** add quotes to pip for zsh customers
* **index:** fold support us banner
* **install:** instructions to reduce pydantic package size ([#1077](https://github.com/awslabs/aws-lambda-powertools-python/issues/1077))
* **install:** address early v2 feedback on installation and project support
* **jmespath_util:** snippets split, improved, and lint ([#1419](https://github.com/awslabs/aws-lambda-powertools-python/issues/1419))
* **layer:** upgrade to 1.28.0 (v33)
* **layer:** update to 1.25.3
* **layer:** update to 1.25.6; cosmetic changes
* **layer:** update to 1.25.7
* **layer:** update to 1.25.1
* **layer:** remove link from clipboard button ([#1135](https://github.com/awslabs/aws-lambda-powertools-python/issues/1135))
* **layer:** upgrade to 1.25.9
* **layer:** upgrade to 1.25.10
* **layer:** upgrade to 1.26.7
* **layer:** update to 1.24.2
* **layer:** upgrade to 1.27.0
* **layer:** upgrade to 1.27.0
* **layer:** bump to 1.25.5
* **lint:** add markdownlint rules and automation ([#1256](https://github.com/awslabs/aws-lambda-powertools-python/issues/1256))
* **logger:** snippets split, improved, and lint ([#1262](https://github.com/awslabs/aws-lambda-powertools-python/issues/1262))
* **logger:** update uncaught exception message value
* **logger:** document enriching logs with logrecord attributes ([#1271](https://github.com/awslabs/aws-lambda-powertools-python/issues/1271))
* **logger:** fix typo. ([#1587](https://github.com/awslabs/aws-lambda-powertools-python/issues/1587))
* **logger:** Add warning of uncaught exceptions ([#1826](https://github.com/awslabs/aws-lambda-powertools-python/issues/1826))
* **logger:** fix incorrect field names in example structured logs ([#1830](https://github.com/awslabs/aws-lambda-powertools-python/issues/1830))
* **maintainers:** initial maintainers playbook ([#1222](https://github.com/awslabs/aws-lambda-powertools-python/issues/1222))
* **metrics:** snippets split, improved, and lint ([#1272](https://github.com/awslabs/aws-lambda-powertools-python/issues/1272))
* **metrics:** snippets split, improved, and lint
* **metrics:** fix syntax highlighting for new default_dimensions
* **metrics:** remove reduntant wording before release
* **middleware-factory:** snippets split, improved, and lint ([#1451](https://github.com/awslabs/aws-lambda-powertools-python/issues/1451))
* **multiple:** fix highlighting after new isort/black integration
* **parameters:** add testing your code section ([#1017](https://github.com/awslabs/aws-lambda-powertools-python/issues/1017))
* **parameters:** snippets split, improved, and lint ([#1564](https://github.com/awslabs/aws-lambda-powertools-python/issues/1564))
* **parser:** APIGatewayProxyEvent to APIGatewayProxyEventModel ([#1061](https://github.com/awslabs/aws-lambda-powertools-python/issues/1061))
* **parser:** add JSON string field extension example ([#1526](https://github.com/awslabs/aws-lambda-powertools-python/issues/1526))
* **parser:** minor grammar fix ([#1427](https://github.com/awslabs/aws-lambda-powertools-python/issues/1427))
* **plugin:** add mermaid to create diagram as code ([#1070](https://github.com/awslabs/aws-lambda-powertools-python/issues/1070))
* **readme:** add lambda layer latest version badge
* **roadmap:** use pinned pause issue instead
* **roadmap:** refresh roadmap post-v2 launch
* **roadmap:** include observability provider and lambda layer themes before v2
* **roadmap:** add new roadmap section ([#1204](https://github.com/awslabs/aws-lambda-powertools-python/issues/1204))
* **streaming:** fix leftover newline
* **theme:** upgrade mkdocs-material to 8.x ([#1002](https://github.com/awslabs/aws-lambda-powertools-python/issues/1002))
* **tracer:** split and lint code snippets ([#1260](https://github.com/awslabs/aws-lambda-powertools-python/issues/1260))
* **tracer:** snippets split, improved, and lint ([#1261](https://github.com/awslabs/aws-lambda-powertools-python/issues/1261))
* **tracer:** add note on why X-Ray SDK over ADOT closes [#1675](https://github.com/awslabs/aws-lambda-powertools-python/issues/1675)
* **tutorial:** fix broken internal links ([#1000](https://github.com/awslabs/aws-lambda-powertools-python/issues/1000))
* **typing:** snippets split, improved, and lint ([#1465](https://github.com/awslabs/aws-lambda-powertools-python/issues/1465))
* **upgrade_guide:** add latest changes and quick summary ([#1623](https://github.com/awslabs/aws-lambda-powertools-python/issues/1623))
* **v2:** document optional dependencies and local dev ([#1574](https://github.com/awslabs/aws-lambda-powertools-python/issues/1574))
* **validation:** snippets split, improved, and lint ([#1449](https://github.com/awslabs/aws-lambda-powertools-python/issues/1449))
* **validation:** fix broken link; enrich built-in jmespath links ([#1777](https://github.com/awslabs/aws-lambda-powertools-python/issues/1777))
* **we-made-this:** new community content section ([#1650](https://github.com/awslabs/aws-lambda-powertools-python/issues/1650))
* **we-made-this:** add Feature Flags post ([#1939](https://github.com/awslabs/aws-lambda-powertools-python/issues/1939))
* **we-made-this:** add CI/CD using Feature Flags video   ([#1940](https://github.com/awslabs/aws-lambda-powertools-python/issues/1940))

## Features

* **apigateway:** ignore trailing slashes in routes (APIGatewayRestResolver) ([#1609](https://github.com/awslabs/aws-lambda-powertools-python/issues/1609))
* **apigateway:** multiple exceptions in exception_handler ([#1707](https://github.com/awslabs/aws-lambda-powertools-python/issues/1707))
* **batch:** add support to SQS FIFO queues (SqsFifoPartialProcessor) ([#1934](https://github.com/awslabs/aws-lambda-powertools-python/issues/1934))
* **batch:** inject lambda_context if record handler signature accepts it ([#1561](https://github.com/awslabs/aws-lambda-powertools-python/issues/1561))
* **batch:** add async_batch_processor for concurrent processing ([#1724](https://github.com/awslabs/aws-lambda-powertools-python/issues/1724))
* **ci:** add actionlint in pre-commit hook
* **ci:** create reusable changelog generation ([#1418](https://github.com/awslabs/aws-lambda-powertools-python/issues/1418))
* **ci:** create reusable changelog generation
* **ci:** release docs as alpha when doing a pre-release ([#1624](https://github.com/awslabs/aws-lambda-powertools-python/issues/1624))
* **ci:** include changelog generation on docs build
* **data-classes:** replace AttributeValue in DynamoDBStreamEvent with deserialized Python values ([#1619](https://github.com/awslabs/aws-lambda-powertools-python/issues/1619))
* **data-classes:** add KafkaEvent and KafkaEventRecord ([#1485](https://github.com/awslabs/aws-lambda-powertools-python/issues/1485))
* **data_classes:** add KinesisFirehoseEvent ([#1540](https://github.com/awslabs/aws-lambda-powertools-python/issues/1540))
* **event-handler:** new resolvers to fix current_event typing ([#978](https://github.com/awslabs/aws-lambda-powertools-python/issues/978))
* **event-handler:** context support to share data between routers ([#1567](https://github.com/awslabs/aws-lambda-powertools-python/issues/1567))
* **event_handler:** add cookies as 1st class citizen in v2 ([#1487](https://github.com/awslabs/aws-lambda-powertools-python/issues/1487))
* **event_handler:** improved support for headers and cookies in v2 ([#1455](https://github.com/awslabs/aws-lambda-powertools-python/issues/1455))
* **event_handlers:** Add support for Lambda Function URLs ([#1408](https://github.com/awslabs/aws-lambda-powertools-python/issues/1408))
* **event_sources:** extract CloudWatch Logs in Kinesis streams ([#1710](https://github.com/awslabs/aws-lambda-powertools-python/issues/1710))
* **event_sources:** add CloudWatch dashboard custom widget event ([#1474](https://github.com/awslabs/aws-lambda-powertools-python/issues/1474))
* **feature_flags:** Add Time based feature flags actions ([#1846](https://github.com/awslabs/aws-lambda-powertools-python/issues/1846))
* **idempotency:** support methods with the same name (ABCs) by including fully qualified name in v2 ([#1535](https://github.com/awslabs/aws-lambda-powertools-python/issues/1535))
* **idempotency:** handle lambda timeout scenarios for INPROGRESS records ([#1387](https://github.com/awslabs/aws-lambda-powertools-python/issues/1387))
* **layer:** publish SAR v2 via Github actions ([#1585](https://github.com/awslabs/aws-lambda-powertools-python/issues/1585))
* **layers:** add layer balancer script ([#1643](https://github.com/awslabs/aws-lambda-powertools-python/issues/1643))
* **layers:** add support for publishing v2 layer ([#1558](https://github.com/awslabs/aws-lambda-powertools-python/issues/1558))
* **logger:** log_event support event data classes (e.g. S3Event) ([#984](https://github.com/awslabs/aws-lambda-powertools-python/issues/984))
* **logger:** log uncaught exceptions via system's exception hook ([#1727](https://github.com/awslabs/aws-lambda-powertools-python/issues/1727))
* **logger:** introduce POWERTOOLS_DEBUG for internal debugging ([#1572](https://github.com/awslabs/aws-lambda-powertools-python/issues/1572))
* **logger:** include logger name attribute when copy_config_to_registered_logger is used ([#1568](https://github.com/awslabs/aws-lambda-powertools-python/issues/1568))
* **logger:** accept arbitrary keyword=value for ephemeral metadata ([#1658](https://github.com/awslabs/aws-lambda-powertools-python/issues/1658))
* **logger:** add use_rfc3339 and auto-complete formatter opts in Logger ([#1662](https://github.com/awslabs/aws-lambda-powertools-python/issues/1662))
* **logger:** pretty-print JSON when POWERTOOLS_DEV is set ([#1548](https://github.com/awslabs/aws-lambda-powertools-python/issues/1548))
* **logger:** unwrap event from common models if asked to log ([#1778](https://github.com/awslabs/aws-lambda-powertools-python/issues/1778))
* **logger:** add option to clear state per invocation
* **metrics:** add EphemeralMetrics as a non-singleton option ([#1676](https://github.com/awslabs/aws-lambda-powertools-python/issues/1676))
* **metrics:** add default_dimensions to single_metric ([#1880](https://github.com/awslabs/aws-lambda-powertools-python/issues/1880))
* **metrics:** update max user-defined dimensions from 9 to 29 ([#1417](https://github.com/awslabs/aws-lambda-powertools-python/issues/1417))
* **mypy:** complete mypy support for the entire codebase ([#943](https://github.com/awslabs/aws-lambda-powertools-python/issues/943))
* **parameters:** add clear_cache method for providers ([#1194](https://github.com/awslabs/aws-lambda-powertools-python/issues/1194))
* **parameters:** migrate AppConfig to new APIs due to API deprecation ([#1553](https://github.com/awslabs/aws-lambda-powertools-python/issues/1553))
* **parameters:** accept boto3_client to support private endpoints and ease testing ([#1096](https://github.com/awslabs/aws-lambda-powertools-python/issues/1096))
* **parameters:** add get_parameters_by_name for SSM params in distinct paths ([#1678](https://github.com/awslabs/aws-lambda-powertools-python/issues/1678))
* **parser:** extract CloudWatch Logs in Kinesis streams ([#1726](https://github.com/awslabs/aws-lambda-powertools-python/issues/1726))
* **parser:** export Pydantic.errors through escape hatch ([#1728](https://github.com/awslabs/aws-lambda-powertools-python/issues/1728))
* **parser:** add support for Lambda Function URL ([#1442](https://github.com/awslabs/aws-lambda-powertools-python/issues/1442))
* **parser:** add KinesisFirehoseModel ([#1556](https://github.com/awslabs/aws-lambda-powertools-python/issues/1556))
* **parser:** add KafkaMskEventModel and KafkaSelfManagedEventModel ([#1499](https://github.com/awslabs/aws-lambda-powertools-python/issues/1499))
* **streaming:** add new s3 streaming utility ([#1719](https://github.com/awslabs/aws-lambda-powertools-python/issues/1719))
* **tracer:** support methods with the same name (ABCs) by including fully qualified name in v2 ([#1486](https://github.com/awslabs/aws-lambda-powertools-python/issues/1486))

## Maintenance

* update v2 layer ARN on documentation
* bump to 1.26.2
* bump version 1.26.1
* add sam build gitignore
* move to approach B for multiple IaC
* update v2 layer ARN on documentation
* update v2 layer ARN on documentation
* remove unnecessary test
* bump to version 1.26.3
* update v2 layer ARN on documentation
* update v2 layer ARN on documentation
* bump to 1.26.0
* update v2 layer ARN on documentation
* use isinstance over type
* merge v2 branch
* bump pyproject version to 2.0
* apigw test event wrongly set with base64
* add dummy v2 sar deploy job
* update v2 layer ARN on documentation
* bump layer version to 38
* correct docs
* bump to 1.25.2
* bump to 1.25.3
* lint unused import
* comment reason for change
* update v2 layer ARN on documentation
* remove duplicate test
* bump to 1.25.4
* bump to 1.25.1
* update v2 layer ARN on documentation
* test build layer hardware to 8 core
* update v2 layer ARN on documentation
* bump to 1.25.0
* include regression in changelog
* bump to 1.25.10
* update v2 layer ARN on documentation
* bump to 1.25.6
* dummy for PR test
* update v2 layer ARN on documentation
* print full event depth
* print full workflow event depth
* debug full event
* bump to 1.25.7
* correct docs
* update v2 layer ARN on documentation
* bump to 1.25.5
* bump to 1.25.8
* bump to 1.25.9
* remove leftover from fork one more time
* update v2 layer ARN on documentation
* update v2 layer ARN on documentation
* **batch:** deprecate sqs_batch_processor ([#1463](https://github.com/awslabs/aws-lambda-powertools-python/issues/1463))
* **ci:** remove core group from codeowners ([#1358](https://github.com/awslabs/aws-lambda-powertools-python/issues/1358))
* **ci:** update project with version 1.26.6
* **ci:** use OIDC and encrypt release secrets ([#1355](https://github.com/awslabs/aws-lambda-powertools-python/issues/1355))
* **ci:** add conditional to skip pypi release ([#1366](https://github.com/awslabs/aws-lambda-powertools-python/issues/1366))
* **ci:** update project with version 1.26.6
* **ci:** introduce codeowners ([#1352](https://github.com/awslabs/aws-lambda-powertools-python/issues/1352))
* **ci:** update project with version 1.26.6
* **ci:** increase skip_pypi logic to cover tests/changelog on re-run failures
* **ci:** remove leftover logic from on_merged_pr workflow
* **ci:** post release on tagged issues too
* **ci:** drop 3.6 from workflows
* **ci:** drop 3.6 from workflows ([#1395](https://github.com/awslabs/aws-lambda-powertools-python/issues/1395))
* **ci:** disable mergify configuration after breaking changes ([#1188](https://github.com/awslabs/aws-lambda-powertools-python/issues/1188))
* **ci:** move changelog generation to rebuild_latest_doc workflow
* **ci:** update project with version
* **ci:** move changelog generation to rebuild_latest_doc workflow
* **ci:** readd changelog step on release
* **ci:** update release automated activities
* **ci:** lockdown workflow_run by origin ([#1350](https://github.com/awslabs/aws-lambda-powertools-python/issues/1350))
* **ci:** update changelog with latest changes
* **ci:** test upstream job skip
* **ci:** update changelog with latest changes
* **ci:** add manual trigger for docs
* **ci:** test env expr
* **ci:** update changelog with latest changes
* **ci:** sync area labels to prevent dedup
* **ci:** update changelog with latest changes
* **ci:** test default env
* **ci:** update changelog with latest changes
* **ci:** update changelog with latest changes
* **ci:** reduce payload and only send prod notification
* **ci:** remove area/utilities conflicting label
* **ci:** remove conventional changelog commit to reduce noise
* **ci:** experiment hardening origin
* **ci:** use gh environment for beta and prod layer deploy ([#1356](https://github.com/awslabs/aws-lambda-powertools-python/issues/1356))
* **ci:** experiment hardening origin
* **ci:** confirm workflow_run event
* **ci:** temp disable e2e matrix
* **ci:** include py version in stack and cache lock
* **ci:** revert e2e py version matrix
* **ci:** disable e2e py version matrix due to concurrent locking
* **ci:** update changelog with latest changes
* **ci:** limit E2E workflow run for source code change
* **ci:** remove unused and undeclared OS matrix env
* **ci:** add missing description fields
* **ci:** fix invalid dependency leftover
* **ci:** remove dangling debug step
* **ci:** add linter for GitHub Actions as pre-commit hook ([#1479](https://github.com/awslabs/aws-lambda-powertools-python/issues/1479))
* **ci:** re-create versioned API docs for new pages deployment
* **ci:** re-create versioned API docs for new pages deployment
* **ci:** increase permission in parent job for docs publishing
* **ci:** attempt gh-pages deployment via beta route
* **ci:** changelog pre-generation to fetch tags from origin
* **ci:** update project with version 1.26.5
* **ci:** add workflow to suggest splitting large PRs ([#1480](https://github.com/awslabs/aws-lambda-powertools-python/issues/1480))
* **ci:** enable ci checks for v2
* **ci:** record pr details upon labeling
* **ci:** destructure assignment on comment_large_pr
* **ci:** add note for state persistence on comment_large_pr
* **ci:** format comment  on comment_large_pr script
* **ci:** create reusable docs publishing workflow ([#1482](https://github.com/awslabs/aws-lambda-powertools-python/issues/1482))
* **ci:** create docs workflow for v2
* **ci:** create adhoc docs workflow for v2
* **ci:** adds caching when installing python dependencies ([#1311](https://github.com/awslabs/aws-lambda-powertools-python/issues/1311))
* **ci:** update project with version 1.26.4
* **ci:** create adhoc docs workflow for v2
* **ci:** increase release automation and limit to one manual step ([#1297](https://github.com/awslabs/aws-lambda-powertools-python/issues/1297))
* **ci:** lockdown 3rd party workflows to pin sha ([#1301](https://github.com/awslabs/aws-lambda-powertools-python/issues/1301))
* **ci:** bump hardware for build steps
* **ci:** try bigger hardware for e2e test
* **ci:** uncomment test pypi, fix version bump sync
* **ci:** sync package version with pypi
* **ci:** automatically add area label based on title ([#1300](https://github.com/awslabs/aws-lambda-powertools-python/issues/1300))
* **ci:** disable v2 docs
* **ci:** experiment with conditional on outputs
* **ci:** improve error handling for non-issue numbers
* **ci:** prevent concurrent git update in critical workflows ([#1478](https://github.com/awslabs/aws-lambda-powertools-python/issues/1478))
* **ci:** add end to end testing mechanism ([#1247](https://github.com/awslabs/aws-lambda-powertools-python/issues/1247))
* **ci:** disable output debugging as pr body isnt accepted
* **ci:** auto-merge cdk lib and lambda layer construct
* **ci:** move all scripts under .github/scripts
* **ci:** make export PR reusable
* **ci:** convert inline gh-script to file
* **ci:** migrate E2E tests to CDK CLI and off Docker ([#1501](https://github.com/awslabs/aws-lambda-powertools-python/issues/1501))
* **ci:** fix reference error in related_issue
* **ci:** revert custom hw for E2E due to lack of hw
* **ci:** prevent dependabot updates to trigger E2E
* **ci:** use new custom hw for E2E
* **ci:** limit to src only to prevent dependabot failures
* **ci:** remove v1 workflows ([#1617](https://github.com/awslabs/aws-lambda-powertools-python/issues/1617))
* **ci:** limits concurrency for docs workflow
* **ci:** fix reference error in related_issue
* **ci:** limits concurrency for docs workflow
* **ci:** reactivate on_merged_pr workflow
* **ci:** make release process manual
* **ci:** improve wording on closed issues action
* **ci:** deactivate on_merged_pr workflow
* **ci:** fix typo on version description
* **ci:** move error prone env to code as constants
* **ci:** temporarily disable changelog push on release
* **common:** reusable function to extract event from models
* **core:** expose modules in the Top-level package ([#1517](https://github.com/awslabs/aws-lambda-powertools-python/issues/1517))
* **dep:** add cfn-lint as a dev dependency; pre-commit ([#1612](https://github.com/awslabs/aws-lambda-powertools-python/issues/1612))
* **dep:** bump pyproject to pypi sync
* **deps:** bump aws-xray-sdk from 2.10.0 to 2.11.0 ([#1730](https://github.com/awslabs/aws-lambda-powertools-python/issues/1730))
* **deps:** bump actions/checkout from 2 to 3 ([#1052](https://github.com/awslabs/aws-lambda-powertools-python/issues/1052))
* **deps:** bump dependabot/fetch-metadata from 1.1.1 to 1.3.2 ([#1269](https://github.com/awslabs/aws-lambda-powertools-python/issues/1269))
* **deps:** bump aws-xray-sdk from 2.9.0 to 2.10.0 ([#1270](https://github.com/awslabs/aws-lambda-powertools-python/issues/1270))
* **deps:** bump dependabot/fetch-metadata from 1.3.2 to 1.3.3 ([#1273](https://github.com/awslabs/aws-lambda-powertools-python/issues/1273))
* **deps:** bump docker/setup-qemu-action from 2.0.0 to 2.1.0 ([#1627](https://github.com/awslabs/aws-lambda-powertools-python/issues/1627))
* **deps:** bump docker/setup-buildx-action from 2.4.0 to 2.4.1 ([#1903](https://github.com/awslabs/aws-lambda-powertools-python/issues/1903))
* **deps:** bump peaceiris/actions-gh-pages from 3.8.0 to 3.9.0 ([#1649](https://github.com/awslabs/aws-lambda-powertools-python/issues/1649))
* **deps:** bump actions/setup-node from 2 to 3 ([#1281](https://github.com/awslabs/aws-lambda-powertools-python/issues/1281))
* **deps:** bump actions/setup-python from 2.3.1 to 3 ([#1048](https://github.com/awslabs/aws-lambda-powertools-python/issues/1048))
* **deps:** bump pydantic from 1.9.0 to 1.9.1 ([#1221](https://github.com/awslabs/aws-lambda-powertools-python/issues/1221))
* **deps:** bump dependabot/fetch-metadata from 1.3.4 to 1.3.5 ([#1689](https://github.com/awslabs/aws-lambda-powertools-python/issues/1689))
* **deps:** bump cdk-lambda-powertools-python-layer ([#1284](https://github.com/awslabs/aws-lambda-powertools-python/issues/1284))
* **deps:** bump attrs from 21.2.0 to 21.4.0 ([#1282](https://github.com/awslabs/aws-lambda-powertools-python/issues/1282))
* **deps:** bump jsii from 1.61.0 to 1.62.0 ([#1294](https://github.com/awslabs/aws-lambda-powertools-python/issues/1294))
* **deps:** bump docker/setup-buildx-action from 2.0.0 to 2.4.0 ([#1873](https://github.com/awslabs/aws-lambda-powertools-python/issues/1873))
* **deps:** bump constructs from 10.1.1 to 10.1.46 ([#1306](https://github.com/awslabs/aws-lambda-powertools-python/issues/1306))
* **deps:** bump fastjsonschema from 2.15.3 to 2.16.1 ([#1309](https://github.com/awslabs/aws-lambda-powertools-python/issues/1309))
* **deps:** bump constructs from 10.1.1 to 10.1.49 ([#1308](https://github.com/awslabs/aws-lambda-powertools-python/issues/1308))
* **deps:** bump package to 2.2.0
* **deps:** remove email-validator; use Str over EmailStr in SES model ([#1608](https://github.com/awslabs/aws-lambda-powertools-python/issues/1608))
* **deps:** bump release-drafter/release-drafter from 5.21.0 to 5.21.1 ([#1611](https://github.com/awslabs/aws-lambda-powertools-python/issues/1611))
* **deps:** lock importlib to 4.x
* **deps:** bump email-validator from 1.1.3 to 1.2.1 ([#1199](https://github.com/awslabs/aws-lambda-powertools-python/issues/1199))
* **deps:** bump constructs from 10.1.1 to 10.1.51 ([#1323](https://github.com/awslabs/aws-lambda-powertools-python/issues/1323))
* **deps:** bump actions/github-script from 5 to 6 ([#1023](https://github.com/awslabs/aws-lambda-powertools-python/issues/1023))
* **deps:** bump constructs from 10.1.1 to 10.1.52 ([#1343](https://github.com/awslabs/aws-lambda-powertools-python/issues/1343))
* **deps:** bump dependabot/fetch-metadata from 1.3.5 to 1.3.6 ([#1855](https://github.com/awslabs/aws-lambda-powertools-python/issues/1855))
* **deps:** bump peaceiris/actions-gh-pages from 3.9.1 to 3.9.2 ([#1841](https://github.com/awslabs/aws-lambda-powertools-python/issues/1841))
* **deps:** bump fastjsonschema from 2.15.2 to 2.15.3 ([#949](https://github.com/awslabs/aws-lambda-powertools-python/issues/949))
* **deps:** bump zgosalvez/github-actions-ensure-sha-pinned-actions from 2.0.4 to 2.0.5 ([#1837](https://github.com/awslabs/aws-lambda-powertools-python/issues/1837))
* **deps:** bump future from 0.18.2 to 0.18.3 ([#1836](https://github.com/awslabs/aws-lambda-powertools-python/issues/1836))
* **deps:** bump zgosalvez/github-actions-ensure-sha-pinned-actions from 2.0.3 to 2.0.4 ([#1821](https://github.com/awslabs/aws-lambda-powertools-python/issues/1821))
* **deps:** bump peaceiris/actions-gh-pages from 3.9.0 to 3.9.1 ([#1814](https://github.com/awslabs/aws-lambda-powertools-python/issues/1814))
* **deps:** bump pydantic from 1.10.2 to 1.10.4 ([#1817](https://github.com/awslabs/aws-lambda-powertools-python/issues/1817))
* **deps:** bump pydantic from 1.10.4 to 1.10.5 ([#1931](https://github.com/awslabs/aws-lambda-powertools-python/issues/1931))
* **deps:** bump constructs from 10.1.1 to 10.1.59 ([#1396](https://github.com/awslabs/aws-lambda-powertools-python/issues/1396))
* **deps:** bump jsii from 1.57.0 to 1.63.1 ([#1390](https://github.com/awslabs/aws-lambda-powertools-python/issues/1390))
* **deps:** bump jsii from 1.57.0 to 1.63.2 ([#1400](https://github.com/awslabs/aws-lambda-powertools-python/issues/1400))
* **deps:** bump dependabot/fetch-metadata from 1.3.3 to 1.3.4 ([#1565](https://github.com/awslabs/aws-lambda-powertools-python/issues/1565))
* **deps:** bump constructs from 10.1.1 to 10.1.60 ([#1399](https://github.com/awslabs/aws-lambda-powertools-python/issues/1399))
* **deps:** bump constructs from 10.1.1 to 10.1.63 ([#1402](https://github.com/awslabs/aws-lambda-powertools-python/issues/1402))
* **deps:** bump attrs from 21.4.0 to 22.1.0 ([#1397](https://github.com/awslabs/aws-lambda-powertools-python/issues/1397))
* **deps:** bump constructs from 10.1.1 to 10.1.64 ([#1405](https://github.com/awslabs/aws-lambda-powertools-python/issues/1405))
* **deps:** bump constructs from 10.1.1 to 10.1.65 ([#1407](https://github.com/awslabs/aws-lambda-powertools-python/issues/1407))
* **deps:** bump codecov/codecov-action from 3.0.0 to 3.1.0 ([#1143](https://github.com/awslabs/aws-lambda-powertools-python/issues/1143))
* **deps:** bump gitpython from 3.1.29 to 3.1.30 ([#1812](https://github.com/awslabs/aws-lambda-powertools-python/issues/1812))
* **deps:** bump constructs from 10.1.1 to 10.1.66 ([#1414](https://github.com/awslabs/aws-lambda-powertools-python/issues/1414))
* **deps:** bump actions/setup-python from 3 to 4 ([#1528](https://github.com/awslabs/aws-lambda-powertools-python/issues/1528))
* **deps:** bump release-drafter/release-drafter from 5.21.1 to 5.22.0 ([#1802](https://github.com/awslabs/aws-lambda-powertools-python/issues/1802))
* **deps:** bump email-validator from 1.2.1 to 1.3.0 ([#1533](https://github.com/awslabs/aws-lambda-powertools-python/issues/1533))
* **deps:** bump zgosalvez/github-actions-ensure-sha-pinned-actions from 2.0.1 to 2.0.3 ([#1801](https://github.com/awslabs/aws-lambda-powertools-python/issues/1801))
* **deps:** bump fastjsonschema from 2.16.1 to 2.16.2 ([#1530](https://github.com/awslabs/aws-lambda-powertools-python/issues/1530))
* **deps:** bump codecov/codecov-action from 3.1.0 to 3.1.1 ([#1529](https://github.com/awslabs/aws-lambda-powertools-python/issues/1529))
* **deps:** bump pydantic from 1.9.1 to 1.9.2 ([#1448](https://github.com/awslabs/aws-lambda-powertools-python/issues/1448))
* **deps:** bump release-drafter/release-drafter from 5.20.0 to 5.20.1 ([#1458](https://github.com/awslabs/aws-lambda-powertools-python/issues/1458))
* **deps:** bump release-drafter/release-drafter from 5.20.1 to 5.21.0 ([#1520](https://github.com/awslabs/aws-lambda-powertools-python/issues/1520))
* **deps:** bump codecov/codecov-action from 2.1.0 to 3.0.0 ([#1102](https://github.com/awslabs/aws-lambda-powertools-python/issues/1102))
* **deps:** bump certifi from 2022.9.24 to 2022.12.7 ([#1768](https://github.com/awslabs/aws-lambda-powertools-python/issues/1768))
* **deps:** bump actions/upload-artifact from 2 to 3 ([#1103](https://github.com/awslabs/aws-lambda-powertools-python/issues/1103))
* **deps:** bump zgosalvez/github-actions-ensure-sha-pinned-actions from 2.0.5 to 2.1.0 ([#1943](https://github.com/awslabs/aws-lambda-powertools-python/issues/1943))
* **deps:** bump github/codeql-action from 1 to 2 ([#1154](https://github.com/awslabs/aws-lambda-powertools-python/issues/1154))
* **deps:** bump zgosalvez/github-actions-ensure-sha-pinned-actions from 1.4.0 to 2.0.1 ([#1752](https://github.com/awslabs/aws-lambda-powertools-python/issues/1752))
* **deps:** bump zgosalvez/github-actions-ensure-sha-pinned-actions from 1.3.0 to 1.4.0 ([#1749](https://github.com/awslabs/aws-lambda-powertools-python/issues/1749))
* **deps:** bump aws-cdk-lib from 2.29.0 to 2.31.1 ([#1290](https://github.com/awslabs/aws-lambda-powertools-python/issues/1290))
* **deps:** bump actions/setup-python from 3 to 4 ([#1244](https://github.com/awslabs/aws-lambda-powertools-python/issues/1244))
* **deps-dev:** bump mypy-boto3-xray from 1.26.9 to 1.26.11.post1 ([#1734](https://github.com/awslabs/aws-lambda-powertools-python/issues/1734))
* **deps-dev:** bump mkdocs-material from 8.5.9 to 8.5.10 ([#1731](https://github.com/awslabs/aws-lambda-powertools-python/issues/1731))
* **deps-dev:** bump mypy-boto3-dynamodb from 1.24.55.post1 to 1.24.60 ([#306](https://github.com/awslabs/aws-lambda-powertools-python/issues/306))
* **deps-dev:** bump mkdocs-material from 8.4.1 to 8.4.2 ([#1483](https://github.com/awslabs/aws-lambda-powertools-python/issues/1483))
* **deps-dev:** bump types-requests from 2.28.11.4 to 2.28.11.5 ([#1729](https://github.com/awslabs/aws-lambda-powertools-python/issues/1729))
* **deps-dev:** bump mypy-boto3-ssm from 1.26.4 to 1.26.11.post1 ([#1740](https://github.com/awslabs/aws-lambda-powertools-python/issues/1740))
* **deps-dev:** bump mypy-boto3-secretsmanager from 1.26.0.post1 to 1.26.12 ([#1744](https://github.com/awslabs/aws-lambda-powertools-python/issues/1744))
* **deps-dev:** bump mypy-boto3-dynamodb from 1.26.0.post1 to 1.26.13.post16 ([#1743](https://github.com/awslabs/aws-lambda-powertools-python/issues/1743))
* **deps-dev:** bump aws-cdk-lib from 2.50.0 to 2.51.1 ([#1741](https://github.com/awslabs/aws-lambda-powertools-python/issues/1741))
* **deps-dev:** bump flake8-builtins from 2.0.0 to 2.0.1 ([#1715](https://github.com/awslabs/aws-lambda-powertools-python/issues/1715))
* **deps-dev:** bump mypy-boto3-lambda from 1.26.0.post1 to 1.26.12 ([#1742](https://github.com/awslabs/aws-lambda-powertools-python/issues/1742))
* **deps-dev:** bump mypy-boto3-cloudformation from 1.26.0.post1 to 1.26.11.post1 ([#1746](https://github.com/awslabs/aws-lambda-powertools-python/issues/1746))
* **deps-dev:** revert to v1.28.0 dependencies
* **deps-dev:** bump mypy-boto3-cloudwatch from 1.26.0.post1 to 1.26.17 ([#1753](https://github.com/awslabs/aws-lambda-powertools-python/issues/1753))
* **deps-dev:** bump flake8-black from 0.3.3 to 0.3.5 ([#1738](https://github.com/awslabs/aws-lambda-powertools-python/issues/1738))
* **deps-dev:** bump pytest-asyncio from 0.20.1 to 0.20.2 ([#1723](https://github.com/awslabs/aws-lambda-powertools-python/issues/1723))
* **deps-dev:** bump importlib-metadata from 4.13.0 to 5.1.0 ([#1750](https://github.com/awslabs/aws-lambda-powertools-python/issues/1750))
* **deps-dev:** bump mkdocs-material from 8.5.10 to 8.5.11 ([#1756](https://github.com/awslabs/aws-lambda-powertools-python/issues/1756))
* **deps-dev:** bump mypy-boto3-appconfig from 1.25.0 to 1.26.0.post1 ([#1722](https://github.com/awslabs/aws-lambda-powertools-python/issues/1722))
* **deps-dev:** bump pytest-benchmark from 3.4.1 to 4.0.0 ([#1659](https://github.com/awslabs/aws-lambda-powertools-python/issues/1659))
* **deps-dev:** bump filelock from 3.8.0 to 3.8.2 ([#1759](https://github.com/awslabs/aws-lambda-powertools-python/issues/1759))
* **deps-dev:** bump flake8-bugbear from 22.10.27 to 22.12.6 ([#1760](https://github.com/awslabs/aws-lambda-powertools-python/issues/1760))
* **deps-dev:** bump aws-cdk-lib from 2.53.0 to 2.54.0 ([#1764](https://github.com/awslabs/aws-lambda-powertools-python/issues/1764))
* **deps-dev:** bump mypy-boto3-logs from 1.26.17 to 1.26.27 ([#1775](https://github.com/awslabs/aws-lambda-powertools-python/issues/1775))
* **deps-dev:** bump flake8-bugbear from 22.8.22 to 22.8.23 ([#1473](https://github.com/awslabs/aws-lambda-powertools-python/issues/1473))
* **deps-dev:** bump mypy-boto3-dynamodb from 1.26.13.post16 to 1.26.24 ([#1765](https://github.com/awslabs/aws-lambda-powertools-python/issues/1765))
* **deps-dev:** bump mkdocs-material from 8.4.4 to 8.5.0 ([#1514](https://github.com/awslabs/aws-lambda-powertools-python/issues/1514))
* **deps-dev:** bump black from 21.12b0 to 22.8.0 ([#1515](https://github.com/awslabs/aws-lambda-powertools-python/issues/1515))
* **deps-dev:** bump mypy-boto3-dynamodb from 1.24.60 to 1.24.74 ([#1522](https://github.com/awslabs/aws-lambda-powertools-python/issues/1522))
* **deps-dev:** bump mkdocs-material from 8.5.0 to 8.5.1 ([#1521](https://github.com/awslabs/aws-lambda-powertools-python/issues/1521))
* **deps-dev:** bump pytest from 6.2.5 to 7.0.1 ([#1063](https://github.com/awslabs/aws-lambda-powertools-python/issues/1063))
* **deps-dev:** bump mypy-boto3-s3 from 1.24.36.post1 to 1.24.76 ([#1531](https://github.com/awslabs/aws-lambda-powertools-python/issues/1531))
* **deps-dev:** bump aws-cdk-lib from 2.49.0 to 2.50.0 ([#1683](https://github.com/awslabs/aws-lambda-powertools-python/issues/1683))
* **deps-dev:** bump pytest-asyncio from 0.20.2 to 0.20.3 ([#1767](https://github.com/awslabs/aws-lambda-powertools-python/issues/1767))
* **deps-dev:** bump isort from 5.10.1 to 5.11.2 ([#1782](https://github.com/awslabs/aws-lambda-powertools-python/issues/1782))
* **deps-dev:** bump mkdocs-material from 8.2.4 to 8.2.7 ([#1131](https://github.com/awslabs/aws-lambda-powertools-python/issues/1131))
* **deps-dev:** bump types-requests from 2.28.7 to 2.28.8 ([#1423](https://github.com/awslabs/aws-lambda-powertools-python/issues/1423))
* **deps-dev:** bump mypy-boto3-cloudwatch from 1.26.17 to 1.26.30 ([#1785](https://github.com/awslabs/aws-lambda-powertools-python/issues/1785))
* **deps-dev:** bump aws-cdk-lib from 2.54.0 to 2.55.1 ([#1787](https://github.com/awslabs/aws-lambda-powertools-python/issues/1787))
* **deps-dev:** bump isort from 5.11.2 to 5.11.3 ([#1788](https://github.com/awslabs/aws-lambda-powertools-python/issues/1788))
* **deps-dev:** bump types-requests from 2.28.11.5 to 2.28.11.7 ([#1795](https://github.com/awslabs/aws-lambda-powertools-python/issues/1795))
* **deps-dev:** bump mkdocs-material from 8.5.1 to 8.5.3 ([#1532](https://github.com/awslabs/aws-lambda-powertools-python/issues/1532))
* **deps-dev:** bump flake8-black from 0.3.5 to 0.3.6 ([#1792](https://github.com/awslabs/aws-lambda-powertools-python/issues/1792))
* **deps-dev:** bump black from 22.10.0 to 22.12.0 ([#1770](https://github.com/awslabs/aws-lambda-powertools-python/issues/1770))
* **deps-dev:** bump mypy-boto3-ssm from 1.26.0.post1 to 1.26.4 ([#1721](https://github.com/awslabs/aws-lambda-powertools-python/issues/1721))
* **deps-dev:** bump importlib-metadata from 5.1.0 to 6.0.0 ([#1804](https://github.com/awslabs/aws-lambda-powertools-python/issues/1804))
* **deps-dev:** bump aws-cdk-lib from 2.55.1 to 2.59.0 ([#1810](https://github.com/awslabs/aws-lambda-powertools-python/issues/1810))
* **deps-dev:** bump types-requests from 2.28.10 to 2.28.11 ([#1538](https://github.com/awslabs/aws-lambda-powertools-python/issues/1538))
* **deps-dev:** bump mypy-boto3-secretsmanager from 1.26.12 to 1.26.40 ([#1811](https://github.com/awslabs/aws-lambda-powertools-python/issues/1811))
* **deps-dev:** bump mako from 1.2.2 to 1.2.3 ([#1537](https://github.com/awslabs/aws-lambda-powertools-python/issues/1537))
* **deps-dev:** bump mypy-boto3-ssm from 1.24.69 to 1.24.80 ([#1542](https://github.com/awslabs/aws-lambda-powertools-python/issues/1542))
* **deps-dev:** bump flake8-builtins from 2.0.1 to 2.1.0 ([#1799](https://github.com/awslabs/aws-lambda-powertools-python/issues/1799))
* **deps-dev:** bump mypy from 0.931 to 0.942 ([#1133](https://github.com/awslabs/aws-lambda-powertools-python/issues/1133))
* **deps-dev:** bump xenon from 0.8.0 to 0.9.0 ([#1145](https://github.com/awslabs/aws-lambda-powertools-python/issues/1145))
* **deps-dev:** bump mypy-boto3-ssm from 1.24.80 to 1.24.81 ([#1544](https://github.com/awslabs/aws-lambda-powertools-python/issues/1544))
* **deps-dev:** bump flake8-bugbear from 22.9.11 to 22.9.23 ([#1541](https://github.com/awslabs/aws-lambda-powertools-python/issues/1541))
* **deps-dev:** bump types-requests from 2.28.6 to 2.28.7 ([#1406](https://github.com/awslabs/aws-lambda-powertools-python/issues/1406))
* **deps-dev:** bump pytest-cov from 3.0.0 to 4.0.0 ([#1551](https://github.com/awslabs/aws-lambda-powertools-python/issues/1551))
* **deps-dev:** bump mypy-boto3-xray from 1.26.0.post1 to 1.26.9 ([#1720](https://github.com/awslabs/aws-lambda-powertools-python/issues/1720))
* **deps-dev:** bump mypy-boto3-secretsmanager from 1.24.54 to 1.24.83 ([#1557](https://github.com/awslabs/aws-lambda-powertools-python/issues/1557))
* **deps-dev:** bump types-requests from 2.28.5 to 2.28.6 ([#1401](https://github.com/awslabs/aws-lambda-powertools-python/issues/1401))
* **deps-dev:** bump mkdocs-material from 8.5.3 to 8.5.4 ([#1563](https://github.com/awslabs/aws-lambda-powertools-python/issues/1563))
* **deps-dev:** bump types-requests from 2.28.11 to 2.28.11.1 ([#1571](https://github.com/awslabs/aws-lambda-powertools-python/issues/1571))
* **deps-dev:** bump coverage from 6.5.0 to 7.0.3 ([#1806](https://github.com/awslabs/aws-lambda-powertools-python/issues/1806))
* **deps-dev:** bump mkdocs-material from 8.5.11 to 9.0.2 ([#1808](https://github.com/awslabs/aws-lambda-powertools-python/issues/1808))
* **deps-dev:** bump mypy-boto3-cloudformation from 1.26.11.post1 to 1.26.35.post1 ([#1818](https://github.com/awslabs/aws-lambda-powertools-python/issues/1818))
* **deps-dev:** bump mkdocs-git-revision-date-plugin ([#1146](https://github.com/awslabs/aws-lambda-powertools-python/issues/1146))
* **deps-dev:** bump filelock from 3.8.2 to 3.9.0 ([#1816](https://github.com/awslabs/aws-lambda-powertools-python/issues/1816))
* **deps-dev:** bump mypy-boto3-appconfig from 1.23.0.post1 to 1.24.0 ([#1233](https://github.com/awslabs/aws-lambda-powertools-python/issues/1233))
* **deps-dev:** bump mypy-boto3-lambda from 1.25.0 to 1.26.0.post1 ([#1705](https://github.com/awslabs/aws-lambda-powertools-python/issues/1705))
* **deps-dev:** bump mypy-boto3-s3 from 1.25.0 to 1.26.0.post1 ([#1716](https://github.com/awslabs/aws-lambda-powertools-python/issues/1716))
* **deps-dev:** bump flake8-isort from 4.1.1 to 4.1.2.post0 ([#1384](https://github.com/awslabs/aws-lambda-powertools-python/issues/1384))
* **deps-dev:** bump mypy-boto3-logs from 1.26.27 to 1.26.43 ([#1820](https://github.com/awslabs/aws-lambda-powertools-python/issues/1820))
* **deps-dev:** bump mypy-boto3-ssm from 1.26.11.post1 to 1.26.43 ([#1819](https://github.com/awslabs/aws-lambda-powertools-python/issues/1819))
* **deps-dev:** bump mypy-boto3-appconfigdata from 1.25.0 to 1.26.0.post1 ([#1704](https://github.com/awslabs/aws-lambda-powertools-python/issues/1704))
* **deps-dev:** bump mypy-boto3-xray from 1.25.0 to 1.26.0.post1 ([#1703](https://github.com/awslabs/aws-lambda-powertools-python/issues/1703))
* **deps-dev:** bump isort from 5.11.3 to 5.11.4 ([#1809](https://github.com/awslabs/aws-lambda-powertools-python/issues/1809))
* **deps-dev:** bump ijson from 3.1.4 to 3.2.0.post0 ([#1815](https://github.com/awslabs/aws-lambda-powertools-python/issues/1815))
* **deps-dev:** bump typing-extensions from 4.3.0 to 4.4.0 ([#1575](https://github.com/awslabs/aws-lambda-powertools-python/issues/1575))
* **deps-dev:** bump mkdocs-material from 9.0.2 to 9.0.3 ([#1823](https://github.com/awslabs/aws-lambda-powertools-python/issues/1823))
* **deps-dev:** bump coverage from 7.0.4 to 7.0.5 ([#1829](https://github.com/awslabs/aws-lambda-powertools-python/issues/1829))
* **deps-dev:** bump aws-cdk-lib from 2.59.0 to 2.60.0 ([#1831](https://github.com/awslabs/aws-lambda-powertools-python/issues/1831))
* **deps-dev:** bump mypy-boto3-lambda from 1.26.18 to 1.26.49 ([#1832](https://github.com/awslabs/aws-lambda-powertools-python/issues/1832))
* **deps-dev:** bump mypy-boto3-secretsmanager from 1.26.40 to 1.26.49 ([#1835](https://github.com/awslabs/aws-lambda-powertools-python/issues/1835))
* **deps-dev:** bump mypy-boto3-logs from 1.26.43 to 1.26.49 ([#1834](https://github.com/awslabs/aws-lambda-powertools-python/issues/1834))
* **deps-dev:** bump mkdocs-material from 9.0.3 to 9.0.4 ([#1833](https://github.com/awslabs/aws-lambda-powertools-python/issues/1833))
* **deps-dev:** bump types-requests from 2.28.11.1 to 2.28.11.2 ([#1576](https://github.com/awslabs/aws-lambda-powertools-python/issues/1576))
* **deps-dev:** bump mypy-boto3-cloudwatch from 1.25.0 to 1.26.0.post1 ([#1714](https://github.com/awslabs/aws-lambda-powertools-python/issues/1714))
* **deps-dev:** bump mkdocs-material from 9.0.4 to 9.0.5 ([#1840](https://github.com/awslabs/aws-lambda-powertools-python/issues/1840))
* **deps-dev:** bump pytest from 7.2.0 to 7.2.1 ([#1838](https://github.com/awslabs/aws-lambda-powertools-python/issues/1838))
* **deps-dev:** bump flake8-builtins from 1.5.3 to 2.0.0 ([#1582](https://github.com/awslabs/aws-lambda-powertools-python/issues/1582))
* **deps-dev:** bump types-requests from 2.28.11.7 to 2.28.11.8 ([#1843](https://github.com/awslabs/aws-lambda-powertools-python/issues/1843))
* **deps-dev:** bump mypy-boto3-cloudwatch from 1.26.30 to 1.26.52 ([#1847](https://github.com/awslabs/aws-lambda-powertools-python/issues/1847))
* **deps-dev:** bump aws-cdk-lib from 2.60.0 to 2.61.1 ([#1849](https://github.com/awslabs/aws-lambda-powertools-python/issues/1849))
* **deps-dev:** bump mypy-boto3-logs from 1.26.49 to 1.26.53 ([#1850](https://github.com/awslabs/aws-lambda-powertools-python/issues/1850))
* **deps-dev:** bump mkdocs-material from 9.0.5 to 9.0.6 ([#1851](https://github.com/awslabs/aws-lambda-powertools-python/issues/1851))
* **deps-dev:** bump mypy-boto3-lambda from 1.26.49 to 1.26.55 ([#1856](https://github.com/awslabs/aws-lambda-powertools-python/issues/1856))
* **deps-dev:** bump mypy-boto3-ssm from 1.24.81 to 1.24.90 ([#1594](https://github.com/awslabs/aws-lambda-powertools-python/issues/1594))
* **deps-dev:** bump mkdocs-material from 8.1.9 to 8.2.4 ([#1054](https://github.com/awslabs/aws-lambda-powertools-python/issues/1054))
* **deps-dev:** bump mypy-boto3-cloudwatch from 1.24.0 to 1.24.35 ([#1342](https://github.com/awslabs/aws-lambda-powertools-python/issues/1342))
* **deps-dev:** bump flake8-eradicate from 1.2.0 to 1.2.1 ([#1158](https://github.com/awslabs/aws-lambda-powertools-python/issues/1158))
* **deps-dev:** bump mypy from 0.942 to 0.950 ([#1162](https://github.com/awslabs/aws-lambda-powertools-python/issues/1162))
* **deps-dev:** bump flake8-bugbear from 22.1.11 to 22.4.25 ([#1156](https://github.com/awslabs/aws-lambda-powertools-python/issues/1156))
* **deps-dev:** bump aws-cdk-lib from 2.61.1 to 2.62.0 ([#1863](https://github.com/awslabs/aws-lambda-powertools-python/issues/1863))
* **deps-dev:** bump coverage from 7.0.5 to 7.1.0 ([#1862](https://github.com/awslabs/aws-lambda-powertools-python/issues/1862))
* **deps-dev:** bump mypy-boto3-cloudformation from 1.26.35.post1 to 1.26.57 ([#1865](https://github.com/awslabs/aws-lambda-powertools-python/issues/1865))
* **deps-dev:** bump aws-cdk-lib from 2.62.0 to 2.62.1 ([#1866](https://github.com/awslabs/aws-lambda-powertools-python/issues/1866))
* **deps-dev:** bump types-requests from 2.28.11.3 to 2.28.11.4 ([#1701](https://github.com/awslabs/aws-lambda-powertools-python/issues/1701))
* **deps-dev:** bump mypy from 0.961 to 0.971 ([#1320](https://github.com/awslabs/aws-lambda-powertools-python/issues/1320))
* **deps-dev:** bump mypy-boto3-logs from 1.25.0 to 1.26.3 ([#1702](https://github.com/awslabs/aws-lambda-powertools-python/issues/1702))
* **deps-dev:** bump mypy-boto3-s3 from 1.26.0.post1 to 1.26.58 ([#1868](https://github.com/awslabs/aws-lambda-powertools-python/issues/1868))
* **deps-dev:** bump aws-cdk-lib from 2.62.1 to 2.62.2 ([#1869](https://github.com/awslabs/aws-lambda-powertools-python/issues/1869))
* **deps-dev:** bump isort from 5.11.4 to 5.11.5 ([#1875](https://github.com/awslabs/aws-lambda-powertools-python/issues/1875))
* **deps-dev:** bump pytest-xdist from 2.5.0 to 3.0.2 ([#1655](https://github.com/awslabs/aws-lambda-powertools-python/issues/1655))
* **deps-dev:** bump mypy-boto3-s3 from 1.24.76 to 1.24.94 ([#1622](https://github.com/awslabs/aws-lambda-powertools-python/issues/1622))
* **deps-dev:** bump mkdocs-material from 8.5.7 to 8.5.9 ([#1697](https://github.com/awslabs/aws-lambda-powertools-python/issues/1697))
* **deps-dev:** bump aws-cdk-lib from 2.46.0 to 2.47.0 ([#1629](https://github.com/awslabs/aws-lambda-powertools-python/issues/1629))
* **deps-dev:** bump mkdocs-material from 9.0.6 to 9.0.8 ([#1874](https://github.com/awslabs/aws-lambda-powertools-python/issues/1874))
* **deps-dev:** bump flake8-comprehensions from 3.10.0 to 3.10.1 ([#1699](https://github.com/awslabs/aws-lambda-powertools-python/issues/1699))
* **deps-dev:** bump flake8-bugbear from 22.12.6 to 23.1.20 ([#1854](https://github.com/awslabs/aws-lambda-powertools-python/issues/1854))
* **deps-dev:** bump aws-cdk-lib from 2.62.2 to 2.63.0 ([#1887](https://github.com/awslabs/aws-lambda-powertools-python/issues/1887))
* **deps-dev:** bump black from 22.12.0 to 23.1.0 ([#1886](https://github.com/awslabs/aws-lambda-powertools-python/issues/1886))
* **deps-dev:** bump mypy-boto3-appconfig from 1.24.0 to 1.24.29 ([#1295](https://github.com/awslabs/aws-lambda-powertools-python/issues/1295))
* **deps-dev:** bump mypy-boto3-dynamodb from 1.24.12 to 1.24.27 ([#1293](https://github.com/awslabs/aws-lambda-powertools-python/issues/1293))
* **deps-dev:** bump types-requests from 2.28.11.2 to 2.28.11.3 ([#1698](https://github.com/awslabs/aws-lambda-powertools-python/issues/1698))
* **deps-dev:** bump mypy-boto3-secretsmanager from 1.25.0 to 1.26.0.post1 ([#1691](https://github.com/awslabs/aws-lambda-powertools-python/issues/1691))
* **deps-dev:** bump flake8-bugbear from 21.11.29 to 22.1.11 ([#955](https://github.com/awslabs/aws-lambda-powertools-python/issues/955))
* **deps-dev:** bump mypy-boto3-s3 from 1.26.58 to 1.26.62 ([#1889](https://github.com/awslabs/aws-lambda-powertools-python/issues/1889))
* **deps-dev:** bump flake8-bugbear from 22.10.25 to 22.10.27 ([#1665](https://github.com/awslabs/aws-lambda-powertools-python/issues/1665))
* **deps-dev:** bump mypy-boto3-ssm from 1.25.0 to 1.26.0.post1 ([#1690](https://github.com/awslabs/aws-lambda-powertools-python/issues/1690))
* **deps-dev:** bump mkdocs-material from 9.0.9 to 9.0.10 ([#1888](https://github.com/awslabs/aws-lambda-powertools-python/issues/1888))
* **deps-dev:** bump mypy-boto3-ssm from 1.21.34 to 1.23.0.post1 ([#1220](https://github.com/awslabs/aws-lambda-powertools-python/issues/1220))
* **deps-dev:** bump mypy-boto3-appconfig from 1.26.0.post1 to 1.26.63 ([#1895](https://github.com/awslabs/aws-lambda-powertools-python/issues/1895))
* **deps-dev:** bump mkdocs-material from 9.0.10 to 9.0.11 ([#1896](https://github.com/awslabs/aws-lambda-powertools-python/issues/1896))
* **deps-dev:** bump aws-cdk-lib from 2.63.0 to 2.63.2 ([#1904](https://github.com/awslabs/aws-lambda-powertools-python/issues/1904))
* **deps-dev:** bump pytest-asyncio from 0.16.0 to 0.20.1 ([#1635](https://github.com/awslabs/aws-lambda-powertools-python/issues/1635))
* **deps-dev:** bump pytest-xdist from 3.1.0 to 3.2.0 ([#1905](https://github.com/awslabs/aws-lambda-powertools-python/issues/1905))
* **deps-dev:** bump mypy-boto3-appconfig from 1.21.34 to 1.23.0.post1 ([#1219](https://github.com/awslabs/aws-lambda-powertools-python/issues/1219))
* **deps-dev:** bump types-requests from 2.28.11.8 to 2.28.11.12 ([#1906](https://github.com/awslabs/aws-lambda-powertools-python/issues/1906))
* **deps-dev:** bump mypy-boto3-secretsmanager from 1.21.34 to 1.23.0.post1 ([#1218](https://github.com/awslabs/aws-lambda-powertools-python/issues/1218))
* **deps-dev:** bump aws-cdk-lib from 2.63.2 to 2.64.0 ([#1918](https://github.com/awslabs/aws-lambda-powertools-python/issues/1918))
* **deps-dev:** bump mkdocs-material from 9.0.11 to 9.0.12 ([#1919](https://github.com/awslabs/aws-lambda-powertools-python/issues/1919))
* **deps-dev:** bump mypy-boto3-appconfigdata from 1.26.0.post1 to 1.26.70 ([#1925](https://github.com/awslabs/aws-lambda-powertools-python/issues/1925))
* **deps-dev:** bump mypy-boto3-secretsmanager from 1.23.0.post1 to 1.23.8 ([#1225](https://github.com/awslabs/aws-lambda-powertools-python/issues/1225))
* **deps-dev:** bump flake8-bugbear from 23.1.20 to 23.2.13 ([#1924](https://github.com/awslabs/aws-lambda-powertools-python/issues/1924))
* **deps-dev:** bump mypy-boto3-appconfig from 1.26.63 to 1.26.71 ([#1928](https://github.com/awslabs/aws-lambda-powertools-python/issues/1928))
* **deps-dev:** bump flake8-variables-names from 0.0.4 to 0.0.5 ([#1628](https://github.com/awslabs/aws-lambda-powertools-python/issues/1628))
* **deps-dev:** bump flake8-bugbear from 22.6.22 to 22.7.1 ([#1274](https://github.com/awslabs/aws-lambda-powertools-python/issues/1274))
* **deps-dev:** bump aws-cdk-lib from 2.47.0 to 2.48.0 ([#1664](https://github.com/awslabs/aws-lambda-powertools-python/issues/1664))
* **deps-dev:** bump aws-cdk-lib from 2.48.0 to 2.49.0 ([#1671](https://github.com/awslabs/aws-lambda-powertools-python/issues/1671))
* **deps-dev:** bump mypy-boto3-cloudformation from 1.25.0 to 1.26.0.post1 ([#1679](https://github.com/awslabs/aws-lambda-powertools-python/issues/1679))
* **deps-dev:** bump types-requests from 2.28.11.12 to 2.28.11.13 ([#1933](https://github.com/awslabs/aws-lambda-powertools-python/issues/1933))
* **deps-dev:** bump types-python-dateutil from 2.8.19.6 to 2.8.19.7 ([#1932](https://github.com/awslabs/aws-lambda-powertools-python/issues/1932))
* **deps-dev:** bump aws-cdk-lib from 2.64.0 to 2.65.0 ([#1938](https://github.com/awslabs/aws-lambda-powertools-python/issues/1938))
* **deps-dev:** bump flake8-bugbear from 22.4.25 to 22.6.22 ([#1258](https://github.com/awslabs/aws-lambda-powertools-python/issues/1258))
* **deps-dev:** bump mypy-boto3-dynamodb from 1.24.0 to 1.24.12 ([#1255](https://github.com/awslabs/aws-lambda-powertools-python/issues/1255))
* **deps-dev:** bump mypy-boto3-secretsmanager ([#1252](https://github.com/awslabs/aws-lambda-powertools-python/issues/1252))
* **deps-dev:** bump mypy from 0.950 to 0.960 ([#1224](https://github.com/awslabs/aws-lambda-powertools-python/issues/1224))
* **deps-dev:** bump mkdocs-material from 9.0.12 to 9.0.13 ([#1944](https://github.com/awslabs/aws-lambda-powertools-python/issues/1944))
* **deps-dev:** bump mypy from 0.960 to 0.961 ([#1241](https://github.com/awslabs/aws-lambda-powertools-python/issues/1241))
* **deps-dev:** bump mypy-boto3-dynamodb from 1.25.0 to 1.26.0.post1 ([#1682](https://github.com/awslabs/aws-lambda-powertools-python/issues/1682))
* **deps-dev:** bump mypy-boto3-ssm from 1.23.0.post1 to 1.24.0 ([#1231](https://github.com/awslabs/aws-lambda-powertools-python/issues/1231))
* **deps-dev:** bump mypy-boto3-secretsmanager from 1.23.8 to 1.24.0 ([#1232](https://github.com/awslabs/aws-lambda-powertools-python/issues/1232))
* **deps-dev:** bump mypy-boto3-dynamodb from 1.23.0.post1 to 1.24.0 ([#1234](https://github.com/awslabs/aws-lambda-powertools-python/issues/1234))
* **deps-dev:** bump pytest-xdist from 3.0.2 to 3.1.0 ([#1758](https://github.com/awslabs/aws-lambda-powertools-python/issues/1758))
* **deps-dev:** bump mypy-boto3-dynamodb from 1.24.55.post1 to 1.24.60 ([#1481](https://github.com/awslabs/aws-lambda-powertools-python/issues/1481))
* **deps-dev:** bump coverage from 7.0.3 to 7.0.4 ([#1822](https://github.com/awslabs/aws-lambda-powertools-python/issues/1822))
* **docs:** remove v2 banner on top of the docs
* **docs:** remove pause sentence from roadmap ([#1409](https://github.com/awslabs/aws-lambda-powertools-python/issues/1409))
* **docs:** update CHANGELOG for v1.26.7
* **docs:** bump layer version to 36 (1.29.2)
* **docs:** update description to trigger changelog generation
* **docs:** update site name to test ci changelog
* **governance:** address gh reusable workflow limitation
* **governance:** auto-merge mypy-stub dependabot
* **governance:** fix workflow action requirements & syntax
* **governance:** enforce safe scope on pr merge labelling
* **governance:** warn message on closed issues
* **governance:** warn message on closed issues
* **governance:** new ask a question
* **governance:** update bug report to a form
* **governance:** fix on_merged_pr workflow syntax
* **governance:** update docs report to a form
* **governance:** bug report form typo
* **governance:** auto-merge to use squash
* **governance:** auto-merge workflow_dispatch off
* **governance:** remove any step relying on master branch
* **governance:** update emeritus affiliation
* **governance:** fix typo on semantic commit link introduced in [#1](https://github.com/awslabs/aws-lambda-powertools-python/issues/1)aef4
* **governance:** update external non-triage effort disclaimer
* **governance:** add new maintenance issue template for tech debt ([#1326](https://github.com/awslabs/aws-lambda-powertools-python/issues/1326))
* **governance:** update wording tech debt to summary in maintenance template
* **governance:** refresh pull request template sections
* **governance:** add pre-configured dev environment with GitPod.io to ease contributions ([#1403](https://github.com/awslabs/aws-lambda-powertools-python/issues/1403))
* **governance:** new static typing report
* **governance:** update feat request to a form
* **governance:** check for related issue in new PRs
* **governance:** auto-merge on all PR events
* **governance:** remove 'area/' from PR labels
* **governance:** add release label on pr merge
* **governance:** remove devcontainer in favour of gitpod.io ([#1411](https://github.com/awslabs/aws-lambda-powertools-python/issues/1411))
* **governance:** limit build workflow to code changes only
* **governance:** update static typing to a form
* **governance:** remove markdown rendering from docs issue template
* **governance:** update rfc to a form
* **layer:** remove unsused GetFunction permission for the canary
* **layer:** bump to latest version 37
* **layer:** bump to 1.31.1 (v39)
* **layers:** add release pipeline in GitHub Actions ([#1278](https://github.com/awslabs/aws-lambda-powertools-python/issues/1278))
* **layers:** replace layers account secret ([#1329](https://github.com/awslabs/aws-lambda-powertools-python/issues/1329))
* **layers:** expand to all aws commercial regions ([#1324](https://github.com/awslabs/aws-lambda-powertools-python/issues/1324))
* **layers:** bump to 1.26.5
* **layers:** bump to 22 for 1.26.3
* **layers:** upgrade cdk dep hashes to prevent ci fail
* **layers:** add release pipeline in GitHub Actions ([#1278](https://github.com/awslabs/aws-lambda-powertools-python/issues/1278))
* **layers:** bump to 22 for 1.26.3
* **layers:** bump to 10 for 1.25.0
* **layers:** add dummy v2 layer automation
* **layers:** layer canary stack should not hardcode resource name
* **layers:** bump to 1.26.6 using layer v26
* **layers:** bump to 21 for 1.26.2
* **lint:** use new isort black integration
* **logger:** uncaught exception to use exception value as message
* **logger:** overload inject_lambda_context with generics ([#1583](https://github.com/awslabs/aws-lambda-powertools-python/issues/1583))
* **maintainer:** add Leandro as maintainer ([#1468](https://github.com/awslabs/aws-lambda-powertools-python/issues/1468))
* **maintainers:** fix release workflow rename
* **maintainers:** add Ruben as a maintainer ([#1392](https://github.com/awslabs/aws-lambda-powertools-python/issues/1392))
* **maintainers:** update release workflow link
* **maintenance:** add discord link to first PR and first issue ([#1493](https://github.com/awslabs/aws-lambda-powertools-python/issues/1493))
* **metrics:** revert dimensions test before splitting ([#1243](https://github.com/awslabs/aws-lambda-powertools-python/issues/1243))
* **metrics:** fix tests when warnings are disabled ([#994](https://github.com/awslabs/aws-lambda-powertools-python/issues/994))
* **multiple:** localize powertools_dev env logic and warning ([#1570](https://github.com/awslabs/aws-lambda-powertools-python/issues/1570))
* **package:** correct pyproject version manually
* **pypi:** add new links to Pypi package homepage ([#1912](https://github.com/awslabs/aws-lambda-powertools-python/issues/1912))
* **test-perf:** use pytest-benchmark to improve reliability ([#1250](https://github.com/awslabs/aws-lambda-powertools-python/issues/1250))
* **tests:** build and deploy Lambda Layer stack once ([#1466](https://github.com/awslabs/aws-lambda-powertools-python/issues/1466))
* **tests:** enable end-to-end test workflow ([#1470](https://github.com/awslabs/aws-lambda-powertools-python/issues/1470))
* **tests:** move shared_functions to unit tests
* **tests:** refactor E2E test mechanics to ease maintenance, writing tests and parallelization ([#1444](https://github.com/awslabs/aws-lambda-powertools-python/issues/1444))
* **tests:** refactor E2E logger to ease maintenance, writing tests and parallelization ([#1460](https://github.com/awslabs/aws-lambda-powertools-python/issues/1460))
* **tests:** refactor E2E tracer to ease maintenance, writing tests and parallelization ([#1457](https://github.com/awslabs/aws-lambda-powertools-python/issues/1457))

## Regression

* service_name fixture
* **ci:** new gh-pages beta doesn't work either; reverting as gh-pages is disrupted
* **parser:** Add missing fields for SESEvent ([#1027](https://github.com/awslabs/aws-lambda-powertools-python/issues/1027)) ([#1190](https://github.com/awslabs/aws-lambda-powertools-python/issues/1190))


<a name="v1.24.2"></a>
## [v1.24.2] - 2022-01-21
## Bug Fixes

* **data-classes:** underscore support in api gateway authorizer resource name ([#969](https://github.com/awslabs/aws-lambda-powertools-python/issues/969))

## Documentation

* **layer:** update to 1.24.1

## Maintenance

* bump to 1.24.2


<a name="v1.24.1"></a>
## [v1.24.1] - 2022-01-20
## Bug Fixes

* remove unused json import
* remove apigw contract when using event-handler, apigw tracing
* use decorators, split cold start to ease reading
* incorrect log keys, indentation, snippet consistency
* remove f-strings that doesn't evaluate expr
* **batch:** report multiple failures ([#967](https://github.com/awslabs/aws-lambda-powertools-python/issues/967))
* **data-classes:** docstring typos and clean up ([#937](https://github.com/awslabs/aws-lambda-powertools-python/issues/937))
* **parameters:** appconfig internal _get docstrings ([#934](https://github.com/awslabs/aws-lambda-powertools-python/issues/934))

## Documentation

* rename quickstart to tutorial in readme
* rename to tutorial given the size
* add final consideration section
* **batch:** snippet typo on batch processed messages iteration ([#951](https://github.com/awslabs/aws-lambda-powertools-python/issues/951))
* **batch:** fix typo in context manager keyword ([#938](https://github.com/awslabs/aws-lambda-powertools-python/issues/938))
* **homepage:** link to typescript version ([#950](https://github.com/awslabs/aws-lambda-powertools-python/issues/950))
* **install:** new lambda layer for 1.24.0 release
* **metrics:** keep it consistent with other sections, update metric names
* **nav:** make REST and GraphQL event handlers more explicit ([#959](https://github.com/awslabs/aws-lambda-powertools-python/issues/959))
* **quickstart:** expand on intro line
* **quickstart:** tidy requirements up
* **quickstart:** make section agnostic to json lib
* **quickstart:** same process for Logger
* **quickstart:** add sub-sections, fix highlight & code
* **quickstart:** sentence fragmentation, tidy up
* **tenets:** make core, non-core more explicit
* **tracer:** warning to note on local traces
* **tracer:** add initial image, requirements
* **tracer:** add annotation, metadata, and image
* **tracer:** update ServiceLens image w/ API GW, copywriting
* **tutorial:** fix path to images ([#963](https://github.com/awslabs/aws-lambda-powertools-python/issues/963))

## Features

* **ci:** auto-notify & close issues on release
* **logger:** clone powertools logger config to any Python logger ([#927](https://github.com/awslabs/aws-lambda-powertools-python/issues/927))

## Maintenance

* bump to 1.24.1
* bump to 1.24.1
* **ci:** run codeql analysis on push only
* **ci:** fix mergify dependabot queue
* **ci:** add queue name in mergify
* **ci:** remove mergify legacy key
* **ci:** update mergify bot breaking change
* **ci:** safely label PR based on title
* **deps:** bump pydantic from 1.8.2 to 1.9.0 ([#933](https://github.com/awslabs/aws-lambda-powertools-python/issues/933))
* **deps-dev:** bump mypy from 0.930 to 0.931 ([#941](https://github.com/awslabs/aws-lambda-powertools-python/issues/941))

## Regression

* order to APP logger/service name due to screenshots

## Pull Requests

* Merge pull request [#769](https://github.com/awslabs/aws-lambda-powertools-python/issues/769) from mploski/docs/quick-start


<a name="v1.24.0"></a>
## [v1.24.0] - 2021-12-31
## Bug Fixes

* **apigateway:** support [@app](https://github.com/app).not_found() syntax & housekeeping ([#926](https://github.com/awslabs/aws-lambda-powertools-python/issues/926))
* **event-sources:** handle dynamodb null type as none, not bool ([#929](https://github.com/awslabs/aws-lambda-powertools-python/issues/929))
* **warning:** future distutils deprecation ([#921](https://github.com/awslabs/aws-lambda-powertools-python/issues/921))

## Documentation

* consistency around admonitions and snippets ([#919](https://github.com/awslabs/aws-lambda-powertools-python/issues/919))
* Added GraphQL Sample API to Examples section of README.md ([#930](https://github.com/awslabs/aws-lambda-powertools-python/issues/930))
* **batch:** remove leftover from legacy
* **layer:** bump Lambda Layer to version 6
* **tracer:** new ignore_endpoint feature ([#931](https://github.com/awslabs/aws-lambda-powertools-python/issues/931))

## Features

* **event-sources:** cache parsed json in data class ([#909](https://github.com/awslabs/aws-lambda-powertools-python/issues/909))
* **feature_flags:** support beyond boolean values (JSON values) ([#804](https://github.com/awslabs/aws-lambda-powertools-python/issues/804))
* **idempotency:** support dataclasses & pydantic models payloads ([#908](https://github.com/awslabs/aws-lambda-powertools-python/issues/908))
* **logger:** support use_datetime_directive for timestamps ([#920](https://github.com/awslabs/aws-lambda-powertools-python/issues/920))
* **tracer:** ignore tracing for certain hostname(s) or url(s) ([#910](https://github.com/awslabs/aws-lambda-powertools-python/issues/910))

## Maintenance

* bump to 1.24.0
* **deps-dev:** bump mypy from 0.920 to 0.930 ([#925](https://github.com/awslabs/aws-lambda-powertools-python/issues/925))


<a name="v1.23.0"></a>
## [v1.23.0] - 2021-12-20
## Bug Fixes

* **apigateway:** allow list of HTTP methods in route method ([#838](https://github.com/awslabs/aws-lambda-powertools-python/issues/838))
* **event-sources:** Pass authorizer data to APIGatewayEventAuthorizer ([#897](https://github.com/awslabs/aws-lambda-powertools-python/issues/897))
* **event-sources:** handle claimsOverrideDetails set to null ([#878](https://github.com/awslabs/aws-lambda-powertools-python/issues/878))
* **idempotency:** include decorated fn name in hash ([#869](https://github.com/awslabs/aws-lambda-powertools-python/issues/869))
* **metrics:** explicit type to single_metric ctx manager ([#865](https://github.com/awslabs/aws-lambda-powertools-python/issues/865))
* **parameters:** appconfig transform and return types ([#877](https://github.com/awslabs/aws-lambda-powertools-python/issues/877))
* **parser:** overload parse when using envelope ([#885](https://github.com/awslabs/aws-lambda-powertools-python/issues/885))
* **parser:** kinesis sequence number is str, not int ([#907](https://github.com/awslabs/aws-lambda-powertools-python/issues/907))
* **parser:** mypy support for payload type override as models ([#883](https://github.com/awslabs/aws-lambda-powertools-python/issues/883))
* **tracer:** add warm start annotation (ColdStart=False) ([#851](https://github.com/awslabs/aws-lambda-powertools-python/issues/851))

## Documentation

* external reference to cloudformation custom resource helper ([#914](https://github.com/awslabs/aws-lambda-powertools-python/issues/914))
* add new public Slack invite
* disable search blur in non-prod env
* update Lambda Layers version
* **apigateway:** add new not_found feature ([#915](https://github.com/awslabs/aws-lambda-powertools-python/issues/915))
* **apigateway:** fix sample layout provided ([#864](https://github.com/awslabs/aws-lambda-powertools-python/issues/864))
* **appsync:** fix users.py typo to locations [#830](https://github.com/awslabs/aws-lambda-powertools-python/issues/830)
* **lambda_layer:** fix CDK layer syntax

## Features

* **apigateway:** add exception_handler support ([#898](https://github.com/awslabs/aws-lambda-powertools-python/issues/898))
* **apigateway:** access parent api resolver from router ([#842](https://github.com/awslabs/aws-lambda-powertools-python/issues/842))
* **batch:** new BatchProcessor for SQS, DynamoDB, Kinesis ([#886](https://github.com/awslabs/aws-lambda-powertools-python/issues/886))
* **logger:** allow handler with custom kwargs signature ([#913](https://github.com/awslabs/aws-lambda-powertools-python/issues/913))
* **tracer:** add service annotation when service is set ([#861](https://github.com/awslabs/aws-lambda-powertools-python/issues/861))

## Maintenance

* correct pr label order
* minor housekeeping before release ([#912](https://github.com/awslabs/aws-lambda-powertools-python/issues/912))
* bump to 1.23.0
* **ci:** split latest docs workflow
* **deps:** bump fastjsonschema from 2.15.1 to 2.15.2 ([#891](https://github.com/awslabs/aws-lambda-powertools-python/issues/891))
* **deps:** bump actions/setup-python from 2.2.2 to 2.3.0 ([#831](https://github.com/awslabs/aws-lambda-powertools-python/issues/831))
* **deps:** bump aws-xray-sdk from 2.8.0 to 2.9.0 ([#876](https://github.com/awslabs/aws-lambda-powertools-python/issues/876))
* **deps:** support arm64 when developing locally ([#862](https://github.com/awslabs/aws-lambda-powertools-python/issues/862))
* **deps:** bump actions/setup-python from 2.3.0 to 2.3.1 ([#852](https://github.com/awslabs/aws-lambda-powertools-python/issues/852))
* **deps-dev:** bump flake8 from 3.9.2 to 4.0.1 ([#789](https://github.com/awslabs/aws-lambda-powertools-python/issues/789))
* **deps-dev:** bump black from 21.10b0 to 21.11b1 ([#839](https://github.com/awslabs/aws-lambda-powertools-python/issues/839))
* **deps-dev:** bump black from 21.11b1 to 21.12b0 ([#872](https://github.com/awslabs/aws-lambda-powertools-python/issues/872))
* **deps-dev:** bump mypy from 0.910 to 0.920 ([#903](https://github.com/awslabs/aws-lambda-powertools-python/issues/903))


<a name="v1.22.0"></a>
## [v1.22.0] - 2021-11-17
## Bug Fixes

* change supported python version from 3.6.1 to 3.6.2, bump black ([#807](https://github.com/awslabs/aws-lambda-powertools-python/issues/807))
* **ci:** comment custom publish version checker
* **ci:** skip sync master on docs hotfix
* **parser:** body/QS can be null or omitted in apigw v1/v2 ([#820](https://github.com/awslabs/aws-lambda-powertools-python/issues/820))

## Code Refactoring

* **apigateway:** Add BaseRouter and duplicate route check ([#757](https://github.com/awslabs/aws-lambda-powertools-python/issues/757))

## Documentation

* updated Lambda Layers definition & limitations. ([#775](https://github.com/awslabs/aws-lambda-powertools-python/issues/775))
* Idiomatic tenet updated to Progressive
* use higher contrast font ([#822](https://github.com/awslabs/aws-lambda-powertools-python/issues/822))
* use higher contrast font
* fix indentation of SAM snippets in install section ([#778](https://github.com/awslabs/aws-lambda-powertools-python/issues/778))
* improve public lambda layer wording, clipboard buttons ([#762](https://github.com/awslabs/aws-lambda-powertools-python/issues/762))
* add amplify-cli instructions for public layer ([#754](https://github.com/awslabs/aws-lambda-powertools-python/issues/754))
* **api-gateway:** add support for new router feature ([#767](https://github.com/awslabs/aws-lambda-powertools-python/issues/767))
* **apigateway:** re-add sample layout, add considerations ([#826](https://github.com/awslabs/aws-lambda-powertools-python/issues/826))
* **appsync:** add new router feature ([#821](https://github.com/awslabs/aws-lambda-powertools-python/issues/821))
* **idempotency:** add support for DynamoDB composite keys ([#808](https://github.com/awslabs/aws-lambda-powertools-python/issues/808))
* **tenets:** update Idiomatic tenet to Progressive ([#823](https://github.com/awslabs/aws-lambda-powertools-python/issues/823))

## Features

* **apigateway:** add Router to allow large routing composition ([#645](https://github.com/awslabs/aws-lambda-powertools-python/issues/645))
* **appsync:** add Router to allow large resolver composition ([#776](https://github.com/awslabs/aws-lambda-powertools-python/issues/776))
* **data-classes:** ActiveMQ and RabbitMQ support ([#770](https://github.com/awslabs/aws-lambda-powertools-python/issues/770))
* **logger:** add ALB correlation ID support ([#816](https://github.com/awslabs/aws-lambda-powertools-python/issues/816))

## Maintenance

* fix var expr
* remove Lambda Layer version tag
* bump to 1.22.0
* conditional to publish docs only attempt 3
* conditional to publish docs only attempt 2
* conditional to publish docs only
* **deps:** bump boto3 from 1.18.58 to 1.18.59 ([#760](https://github.com/awslabs/aws-lambda-powertools-python/issues/760))
* **deps:** bump boto3 from 1.18.56 to 1.18.58 ([#755](https://github.com/awslabs/aws-lambda-powertools-python/issues/755))
* **deps:** bump urllib3 from 1.26.4 to 1.26.5 ([#787](https://github.com/awslabs/aws-lambda-powertools-python/issues/787))
* **deps:** bump boto3 from 1.19.6 to 1.20.3 ([#809](https://github.com/awslabs/aws-lambda-powertools-python/issues/809))
* **deps:** bump boto3 from 1.18.61 to 1.19.6 ([#783](https://github.com/awslabs/aws-lambda-powertools-python/issues/783))
* **deps:** bump boto3 from 1.20.3 to 1.20.5 ([#817](https://github.com/awslabs/aws-lambda-powertools-python/issues/817))
* **deps:** bump boto3 from 1.18.59 to 1.18.61 ([#766](https://github.com/awslabs/aws-lambda-powertools-python/issues/766))
* **deps-dev:** bump coverage from 6.0.1 to 6.0.2 ([#764](https://github.com/awslabs/aws-lambda-powertools-python/issues/764))
* **deps-dev:** bump pytest-asyncio from 0.15.1 to 0.16.0 ([#782](https://github.com/awslabs/aws-lambda-powertools-python/issues/782))
* **deps-dev:** bump flake8-eradicate from 1.1.0 to 1.2.0 ([#784](https://github.com/awslabs/aws-lambda-powertools-python/issues/784))
* **deps-dev:** bump flake8-isort from 4.0.0 to 4.1.1 ([#785](https://github.com/awslabs/aws-lambda-powertools-python/issues/785))
* **deps-dev:** bump mkdocs-material from 7.3.2 to 7.3.3 ([#758](https://github.com/awslabs/aws-lambda-powertools-python/issues/758))
* **deps-dev:** bump flake8-comprehensions from 3.6.1 to 3.7.0 ([#759](https://github.com/awslabs/aws-lambda-powertools-python/issues/759))
* **deps-dev:** bump mkdocs-material from 7.3.3 to 7.3.5 ([#781](https://github.com/awslabs/aws-lambda-powertools-python/issues/781))
* **deps-dev:** bump coverage from 6.0 to 6.0.1 ([#751](https://github.com/awslabs/aws-lambda-powertools-python/issues/751))
* **deps-dev:** bump mkdocs-material from 7.3.5 to 7.3.6 ([#791](https://github.com/awslabs/aws-lambda-powertools-python/issues/791))
* **deps-dev:** bump coverage from 6.0.2 to 6.1.2 ([#810](https://github.com/awslabs/aws-lambda-powertools-python/issues/810))
* **deps-dev:** bump isort from 5.9.3 to 5.10.1 ([#811](https://github.com/awslabs/aws-lambda-powertools-python/issues/811))


<a name="v1.21.1"></a>
## [v1.21.1] - 2021-10-07
## Documentation

* add new public layer ARNs ([#746](https://github.com/awslabs/aws-lambda-powertools-python/issues/746))

## Maintenance

* include public layers changelog
* bump to 1.21.1
* include regression in changelog
* ignore constants in test cov ([#745](https://github.com/awslabs/aws-lambda-powertools-python/issues/745))
* ignore constants in tests cov
* add support for publishing fallback
* **deps:** bump boto3 from 1.18.54 to 1.18.56 ([#742](https://github.com/awslabs/aws-lambda-powertools-python/issues/742))
* **deps-dev:** bump mkdocs-material from 7.3.1 to 7.3.2 ([#741](https://github.com/awslabs/aws-lambda-powertools-python/issues/741))

## Regression

* **metrics:** typing regression on log_metrics callable ([#744](https://github.com/awslabs/aws-lambda-powertools-python/issues/744))


<a name="v1.21.0"></a>
## [v1.21.0] - 2021-10-05
## Bug Fixes

* **data-classes:** use correct asdict funciton ([#666](https://github.com/awslabs/aws-lambda-powertools-python/issues/666))
* **feature-flags:** rules should evaluate with an AND op ([#724](https://github.com/awslabs/aws-lambda-powertools-python/issues/724))
* **idempotency:** sorting keys before hashing ([#722](https://github.com/awslabs/aws-lambda-powertools-python/issues/722))
* **idempotency:** sorting keys before hashing
* **logger:** push extra keys to the end ([#722](https://github.com/awslabs/aws-lambda-powertools-python/issues/722))
* **mypy:** a few return types, type signatures, and untyped areas ([#718](https://github.com/awslabs/aws-lambda-powertools-python/issues/718))

## Code Refactoring

* **data-classes:** clean up internal logic for APIGatewayAuthorizerResponse ([#643](https://github.com/awslabs/aws-lambda-powertools-python/issues/643))

## Documentation

* Terraform reference for SAR Lambda Layer ([#716](https://github.com/awslabs/aws-lambda-powertools-python/issues/716))
* add team behind it and email
* **event-handler:** document catch-all routes ([#705](https://github.com/awslabs/aws-lambda-powertools-python/issues/705))
* **idempotency:** fix misleading idempotent examples ([#661](https://github.com/awslabs/aws-lambda-powertools-python/issues/661))
* **jmespath:** clarify envelope terminology
* **parser:** fix incorrect import in root_validator example ([#735](https://github.com/awslabs/aws-lambda-powertools-python/issues/735))

## Features

* expose jmespath powertools functions ([#736](https://github.com/awslabs/aws-lambda-powertools-python/issues/736))
* add get_raw_configuration property in store; expose store
* boto3 sessions in batch, parameters & idempotency ([#717](https://github.com/awslabs/aws-lambda-powertools-python/issues/717))
* **feature-flags:** Bring your own logger for debug ([#709](https://github.com/awslabs/aws-lambda-powertools-python/issues/709))
* **feature-flags:** improve "IN/NOT_IN"; new rule actions ([#710](https://github.com/awslabs/aws-lambda-powertools-python/issues/710))
* **feature-flags:** get_raw_configuration property in Store ([#720](https://github.com/awslabs/aws-lambda-powertools-python/issues/720))
* **feature_flags:** Added inequality conditions ([#721](https://github.com/awslabs/aws-lambda-powertools-python/issues/721))
* **idempotency:** makes customers unit testing easier ([#719](https://github.com/awslabs/aws-lambda-powertools-python/issues/719))
* **validator:** include missing data elements from a validation error ([#686](https://github.com/awslabs/aws-lambda-powertools-python/issues/686))

## Maintenance

* add python 3.9 support
* bump to 1.21.0
* **deps:** bump boto3 from 1.18.41 to 1.18.49 ([#703](https://github.com/awslabs/aws-lambda-powertools-python/issues/703))
* **deps:** bump boto3 from 1.18.32 to 1.18.38 ([#671](https://github.com/awslabs/aws-lambda-powertools-python/issues/671))
* **deps:** bump boto3 from 1.18.38 to 1.18.41 ([#677](https://github.com/awslabs/aws-lambda-powertools-python/issues/677))
* **deps:** bump boto3 from 1.18.51 to 1.18.54 ([#733](https://github.com/awslabs/aws-lambda-powertools-python/issues/733))
* **deps:** bump boto3 from 1.18.49 to 1.18.51 ([#713](https://github.com/awslabs/aws-lambda-powertools-python/issues/713))
* **deps:** bump codecov/codecov-action from 2.0.2 to 2.1.0 ([#675](https://github.com/awslabs/aws-lambda-powertools-python/issues/675))
* **deps-dev:** bump flake8-bugbear from 21.9.1 to 21.9.2 ([#712](https://github.com/awslabs/aws-lambda-powertools-python/issues/712))
* **deps-dev:** bump mkdocs-material from 7.3.0 to 7.3.1 ([#731](https://github.com/awslabs/aws-lambda-powertools-python/issues/731))
* **deps-dev:** bump mkdocs-material from 7.2.8 to 7.3.0 ([#695](https://github.com/awslabs/aws-lambda-powertools-python/issues/695))
* **deps-dev:** bump mkdocs-material from 7.2.6 to 7.2.8 ([#682](https://github.com/awslabs/aws-lambda-powertools-python/issues/682))
* **deps-dev:** bump flake8-bugbear from 21.4.3 to 21.9.1 ([#676](https://github.com/awslabs/aws-lambda-powertools-python/issues/676))
* **deps-dev:** bump coverage from 5.5 to 6.0 ([#732](https://github.com/awslabs/aws-lambda-powertools-python/issues/732))
* **deps-dev:** bump radon from 4.5.2 to 5.1.0 ([#673](https://github.com/awslabs/aws-lambda-powertools-python/issues/673))
* **deps-dev:** bump pytest-cov from 2.12.1 to 3.0.0 ([#730](https://github.com/awslabs/aws-lambda-powertools-python/issues/730))
* **deps-dev:** bump xenon from 0.7.3 to 0.8.0 ([#669](https://github.com/awslabs/aws-lambda-powertools-python/issues/669))


<a name="v1.20.2"></a>
## [v1.20.2] - 2021-09-02
## Bug Fixes

* Fix issue with strip_prefixes ([#647](https://github.com/awslabs/aws-lambda-powertools-python/issues/647))

## Maintenance

* bump to 1.20.2
* **deps:** bump boto3 from 1.18.26 to 1.18.32 ([#663](https://github.com/awslabs/aws-lambda-powertools-python/issues/663))
* **deps-dev:** bump mkdocs-material from 7.2.4 to 7.2.6 ([#665](https://github.com/awslabs/aws-lambda-powertools-python/issues/665))
* **deps-dev:** bump pytest from 6.2.4 to 6.2.5 ([#662](https://github.com/awslabs/aws-lambda-powertools-python/issues/662))
* **license:** Add THIRD-PARTY-LICENSES ([#641](https://github.com/awslabs/aws-lambda-powertools-python/issues/641))


<a name="v1.20.1"></a>
## [v1.20.1] - 2021-08-22
## Bug Fixes

* **idempotency:** sorting keys before hashing ([#639](https://github.com/awslabs/aws-lambda-powertools-python/issues/639))

## Maintenance

* bump to 1.20.1
* markdown linter fixes ([#636](https://github.com/awslabs/aws-lambda-powertools-python/issues/636))
* setup codespaces ([#637](https://github.com/awslabs/aws-lambda-powertools-python/issues/637))
* **license:** add third party license ([#635](https://github.com/awslabs/aws-lambda-powertools-python/issues/635))


<a name="v1.20.0"></a>
## [v1.20.0] - 2021-08-21
## Bug Fixes

* **api-gateway:** HTTP API strip stage name from request path ([#622](https://github.com/awslabs/aws-lambda-powertools-python/issues/622))
* **docs:** correct feature_flags link and json exmaples ([#605](https://github.com/awslabs/aws-lambda-powertools-python/issues/605))

## Code Refactoring

* **event_handler:** match to match_results; 3.10 new keyword ([#616](https://github.com/awslabs/aws-lambda-powertools-python/issues/616))

## Documentation

* **api-gateway:** add new API mapping support
* **data-class:** fix invalid syntax in new AppSync Authorizer
* **data-classes:** make authorizer concise; use enum ([#630](https://github.com/awslabs/aws-lambda-powertools-python/issues/630))

## Features

* **data-classes:** authorizer for http api and rest api ([#620](https://github.com/awslabs/aws-lambda-powertools-python/issues/620))
* **data-classes:** data_as_bytes prop KinesisStreamRecordPayload ([#628](https://github.com/awslabs/aws-lambda-powertools-python/issues/628))
* **data-classes:** AppSync Lambda authorizer event ([#610](https://github.com/awslabs/aws-lambda-powertools-python/issues/610))
* **event-handler:** prefixes to strip for custom mappings ([#579](https://github.com/awslabs/aws-lambda-powertools-python/issues/579))
* **general:** support for Python 3.9 ([#626](https://github.com/awslabs/aws-lambda-powertools-python/issues/626))
* **idempotency:** support for any synchronous function ([#625](https://github.com/awslabs/aws-lambda-powertools-python/issues/625))

## Maintenance

* update changelog to reflect out-of-band commits
* bump to 1.20.0
* update new changelog version tag
* **actions:** include new labels
* **api-docs:** enable allow_reuse to fix the docs ([#612](https://github.com/awslabs/aws-lambda-powertools-python/issues/612))
* **deps:** bump boto3 from 1.18.25 to 1.18.26 ([#627](https://github.com/awslabs/aws-lambda-powertools-python/issues/627))
* **deps:** bump boto3 from 1.18.24 to 1.18.25 ([#623](https://github.com/awslabs/aws-lambda-powertools-python/issues/623))
* **deps:** bump boto3 from 1.18.22 to 1.18.24 ([#619](https://github.com/awslabs/aws-lambda-powertools-python/issues/619))
* **deps:** bump boto3 from 1.18.21 to 1.18.22 ([#614](https://github.com/awslabs/aws-lambda-powertools-python/issues/614))
* **deps:** bump boto3 from 1.18.17 to 1.18.21 ([#608](https://github.com/awslabs/aws-lambda-powertools-python/issues/608))
* **deps-dev:** bump flake8-comprehensions from 3.6.0 to 3.6.1 ([#615](https://github.com/awslabs/aws-lambda-powertools-python/issues/615))
* **deps-dev:** bump flake8-comprehensions from 3.5.0 to 3.6.0 ([#609](https://github.com/awslabs/aws-lambda-powertools-python/issues/609))
* **deps-dev:** bump mkdocs-material from 7.2.3 to 7.2.4 ([#607](https://github.com/awslabs/aws-lambda-powertools-python/issues/607))
* **docs:** correct markdown based on markdown lint ([#603](https://github.com/awslabs/aws-lambda-powertools-python/issues/603))
* **shared:** fix cyclic import & refactor data extraction fn ([#613](https://github.com/awslabs/aws-lambda-powertools-python/issues/613))


<a name="v1.19.0"></a>
## [v1.19.0] - 2021-08-11
## Bug Fixes

* **deps:** bump poetry to latest ([#592](https://github.com/awslabs/aws-lambda-powertools-python/issues/592))
* **feature-flags:**  bug handling multiple conditions ([#599](https://github.com/awslabs/aws-lambda-powertools-python/issues/599))
* **feature-toggles:** correct cdk example ([#601](https://github.com/awslabs/aws-lambda-powertools-python/issues/601))
* **parser:** apigw wss validation check_message_id; housekeeping ([#553](https://github.com/awslabs/aws-lambda-powertools-python/issues/553))

## Code Refactoring

* **feature-flags:** add debug for all features evaluation" ([#590](https://github.com/awslabs/aws-lambda-powertools-python/issues/590))
* **feature_flags:** optimize UX and maintenance ([#563](https://github.com/awslabs/aws-lambda-powertools-python/issues/563))

## Documentation

* **event-handler:** new custom serializer option
* **feature-flags:** add guidance when to use vs env vars vs parameters
* **feature-flags:** fix sample feature name in evaluate
* **feature-flags:** create concrete documentation ([#594](https://github.com/awslabs/aws-lambda-powertools-python/issues/594))
* **feature-toggles:** correct docs and typing ([#588](https://github.com/awslabs/aws-lambda-powertools-python/issues/588))
* **feature_flags:** fix SAM infra, convert CDK to Python
* **parameters:** auto-transforming values based on suffix ([#573](https://github.com/awslabs/aws-lambda-powertools-python/issues/573))
* **readme:** add code coverage badge ([#577](https://github.com/awslabs/aws-lambda-powertools-python/issues/577))
* **tracer:** update wording that it auto-disables on non-Lambda env

## Features

* **api-gateway:** add support for custom serializer ([#568](https://github.com/awslabs/aws-lambda-powertools-python/issues/568))
* **data-classes:** decode json_body if based64 encoded ([#560](https://github.com/awslabs/aws-lambda-powertools-python/issues/560))
* **feature flags:** Add not_in action and rename contains to in ([#589](https://github.com/awslabs/aws-lambda-powertools-python/issues/589))
* **params:** expose high level max_age, raise_on_transform_error ([#567](https://github.com/awslabs/aws-lambda-powertools-python/issues/567))
* **tracer:** disable tracer when for non-Lambda envs ([#598](https://github.com/awslabs/aws-lambda-powertools-python/issues/598))

## Maintenance

* only build docs on docs path
* update pypi description, keywords
* bump to 1.19.0
* enable autolabel based on PR title
* include feature-flags docs hotfix
* **deps:** bump boto3 from 1.18.15 to 1.18.17 ([#597](https://github.com/awslabs/aws-lambda-powertools-python/issues/597))
* **deps:** bump boto3 from 1.18.1 to 1.18.15 ([#591](https://github.com/awslabs/aws-lambda-powertools-python/issues/591))
* **deps:** bump codecov/codecov-action from 2.0.1 to 2.0.2 ([#558](https://github.com/awslabs/aws-lambda-powertools-python/issues/558))
* **deps-dev:** bump mkdocs-material from 7.2.1 to 7.2.2 ([#582](https://github.com/awslabs/aws-lambda-powertools-python/issues/582))
* **deps-dev:** bump mkdocs-material from 7.2.2 to 7.2.3 ([#596](https://github.com/awslabs/aws-lambda-powertools-python/issues/596))
* **deps-dev:** bump pdoc3 from 0.9.2 to 0.10.0 ([#584](https://github.com/awslabs/aws-lambda-powertools-python/issues/584))
* **deps-dev:** bump isort from 5.9.2 to 5.9.3 ([#574](https://github.com/awslabs/aws-lambda-powertools-python/issues/574))
* **deps-dev:** bump mkdocs-material from 7.2.0 to 7.2.1 ([#566](https://github.com/awslabs/aws-lambda-powertools-python/issues/566))
* **deps-dev:** bump mkdocs-material from 7.1.11 to 7.2.0 ([#551](https://github.com/awslabs/aws-lambda-powertools-python/issues/551))
* **deps-dev:** bump flake8-black from 0.2.1 to 0.2.3 ([#541](https://github.com/awslabs/aws-lambda-powertools-python/issues/541))


<a name="v1.18.1"></a>
## [v1.18.1] - 2021-07-23
## Bug Fixes

* **api-gateway:** route regression non-word and unsafe URI chars ([#556](https://github.com/awslabs/aws-lambda-powertools-python/issues/556))

## Maintenance

* bump 1.18.1


<a name="v1.18.0"></a>
## [v1.18.0] - 2021-07-20
## Bug Fixes

* **api-gateway:** non-greedy route pattern regex ([#533](https://github.com/awslabs/aws-lambda-powertools-python/issues/533))
* **api-gateway:** incorrect plain text mimetype [#506](https://github.com/awslabs/aws-lambda-powertools-python/issues/506)
* **data-classes:** include milliseconds in scalar types ([#504](https://github.com/awslabs/aws-lambda-powertools-python/issues/504))
* **mypy:** fixes to resolve no implicit optional errors ([#521](https://github.com/awslabs/aws-lambda-powertools-python/issues/521))
* **parser:** Make ApiGateway version, authorizer fields optional ([#532](https://github.com/awslabs/aws-lambda-powertools-python/issues/532))
* **tracer:** mypy generic to preserve decorated method signature ([#529](https://github.com/awslabs/aws-lambda-powertools-python/issues/529))

## Code Refactoring

* **feature-toggles:** Code coverage and housekeeping ([#530](https://github.com/awslabs/aws-lambda-powertools-python/issues/530))

## Documentation

* **api-gateway:** document new HTTP service error exceptions ([#546](https://github.com/awslabs/aws-lambda-powertools-python/issues/546))
* **logger:** document new get_correlation_id method ([#545](https://github.com/awslabs/aws-lambda-powertools-python/issues/545))

## Features

* **api-gateway:** add debug mode ([#507](https://github.com/awslabs/aws-lambda-powertools-python/issues/507))
* **api-gateway:** add common service errors ([#506](https://github.com/awslabs/aws-lambda-powertools-python/issues/506))
* **event-handler:** Support AppSyncResolverEvent subclassing ([#526](https://github.com/awslabs/aws-lambda-powertools-python/issues/526))
* **feat-toggle:** New simple feature toggles rule engine (WIP) ([#494](https://github.com/awslabs/aws-lambda-powertools-python/issues/494))
* **logger:** add get_correlation_id method ([#516](https://github.com/awslabs/aws-lambda-powertools-python/issues/516))
* **mypy:** add mypy support to makefile ([#508](https://github.com/awslabs/aws-lambda-powertools-python/issues/508))

## Maintenance

* bump 1.18.0 ([#547](https://github.com/awslabs/aws-lambda-powertools-python/issues/547))
* **deps:** bump codecov/codecov-action from 1 to 2.0.1 ([#539](https://github.com/awslabs/aws-lambda-powertools-python/issues/539))
* **deps:** bump boto3 from 1.18.0 to 1.18.1 ([#528](https://github.com/awslabs/aws-lambda-powertools-python/issues/528))
* **deps:** bump boto3 from 1.17.110 to 1.18.0 ([#527](https://github.com/awslabs/aws-lambda-powertools-python/issues/527))
* **deps:** bump boto3 from 1.17.102 to 1.17.110 ([#523](https://github.com/awslabs/aws-lambda-powertools-python/issues/523))
* **deps-dev:** bump mkdocs-material from 7.1.10 to 7.1.11 ([#542](https://github.com/awslabs/aws-lambda-powertools-python/issues/542))
* **deps-dev:** bump mkdocs-material from 7.1.9 to 7.1.10 ([#522](https://github.com/awslabs/aws-lambda-powertools-python/issues/522))
* **deps-dev:** bump isort from 5.9.1 to 5.9.2 ([#514](https://github.com/awslabs/aws-lambda-powertools-python/issues/514))
* **event-handler:** adjusts exception docstrings to not confuse AppSync customers


<a name="v1.17.1"></a>
## [v1.17.1] - 2021-07-02
## Bug Fixes

* **validator:** handle built-in custom formats correctly ([#498](https://github.com/awslabs/aws-lambda-powertools-python/issues/498))

## Documentation

* add Layers example for Serverless framework & CDK ([#500](https://github.com/awslabs/aws-lambda-powertools-python/issues/500))
* enable dark mode switch ([#471](https://github.com/awslabs/aws-lambda-powertools-python/issues/471))
* **logger:** add FAQ for cross-account searches ([#501](https://github.com/awslabs/aws-lambda-powertools-python/issues/501))
* **tracer:** additional scenario when to disable auto-capture ([#499](https://github.com/awslabs/aws-lambda-powertools-python/issues/499))

## Maintenance

* bump 1.17.1 ([#502](https://github.com/awslabs/aws-lambda-powertools-python/issues/502))
* **deps:** bump boto3 from 1.17.101 to 1.17.102 ([#493](https://github.com/awslabs/aws-lambda-powertools-python/issues/493))
* **deps:** bump boto3 from 1.17.91 to 1.17.101 ([#490](https://github.com/awslabs/aws-lambda-powertools-python/issues/490))
* **deps:** bump email-validator from 1.1.2 to 1.1.3 ([#478](https://github.com/awslabs/aws-lambda-powertools-python/issues/478))
* **deps:** bump boto3 from 1.17.89 to 1.17.91 ([#473](https://github.com/awslabs/aws-lambda-powertools-python/issues/473))
* **deps-dev:** bump flake8-eradicate from 1.0.0 to 1.1.0 ([#492](https://github.com/awslabs/aws-lambda-powertools-python/issues/492))
* **deps-dev:** bump isort from 5.8.0 to 5.9.1 ([#487](https://github.com/awslabs/aws-lambda-powertools-python/issues/487))
* **deps-dev:** bump mkdocs-material from 7.1.7 to 7.1.9 ([#491](https://github.com/awslabs/aws-lambda-powertools-python/issues/491))


<a name="v1.17.0"></a>
## [v1.17.0] - 2021-06-08
## Documentation

* include new public roadmap ([#452](https://github.com/awslabs/aws-lambda-powertools-python/issues/452))
* **data_classes:** fix missing dynamodb stream get_type/value
* **idempotency:** remove old todo

## Features

* **data-classes:** add AttributeValueType to DynamoDBStreamEvent ([#462](https://github.com/awslabs/aws-lambda-powertools-python/issues/462))
* **data-classes:** decorator to instantiate data_classes and docs updates ([#442](https://github.com/awslabs/aws-lambda-powertools-python/issues/442))
* **logger:** add option to clear state per invocation ([#467](https://github.com/awslabs/aws-lambda-powertools-python/issues/467))
* **parser:** add support for API Gateway HTTP API [#434](https://github.com/awslabs/aws-lambda-powertools-python/issues/434) ([#441](https://github.com/awslabs/aws-lambda-powertools-python/issues/441))

## Maintenance

* bump xenon from 0.7.1 to 0.7.3 ([#446](https://github.com/awslabs/aws-lambda-powertools-python/issues/446))
* fix changelog file redirection
* include dependencies label under maintenance
* ignore codecov upload
* reintroduce codecov token
* fix path for PR auto-labelling
* assited changelog pre-generation, auto-label PR ([#443](https://github.com/awslabs/aws-lambda-powertools-python/issues/443))
* enable dependabot for dep upgrades ([#444](https://github.com/awslabs/aws-lambda-powertools-python/issues/444))
* enable mergify ([#450](https://github.com/awslabs/aws-lambda-powertools-python/issues/450))
* dependabot/mergify guardrail for major versions
* fix dependabot commit messages prefix
* fix dependabot unique set config
* bump mkdocs-material from 7.1.5 to 7.1.6 ([#451](https://github.com/awslabs/aws-lambda-powertools-python/issues/451))
* bump version to 1.17.0
* bump boto3 from 1.17.78 to 1.17.84 ([#449](https://github.com/awslabs/aws-lambda-powertools-python/issues/449))
* update mergify to require approval on dependabot ([#456](https://github.com/awslabs/aws-lambda-powertools-python/issues/456))
* bump actions/setup-python from 1 to 2.2.2 ([#445](https://github.com/awslabs/aws-lambda-powertools-python/issues/445))
* trial boring cyborg automation
* **deps:** bump boto3 from 1.17.87 to 1.17.88 ([#463](https://github.com/awslabs/aws-lambda-powertools-python/issues/463))
* **deps:** bump boto3 from 1.17.88 to 1.17.89 ([#466](https://github.com/awslabs/aws-lambda-powertools-python/issues/466))
* **deps:** bump boto3 from 1.17.84 to 1.17.85 ([#455](https://github.com/awslabs/aws-lambda-powertools-python/issues/455))
* **deps:** bump boto3 from 1.17.85 to 1.17.86 ([#458](https://github.com/awslabs/aws-lambda-powertools-python/issues/458))
* **deps:** bump boto3 from 1.17.86 to 1.17.87 ([#459](https://github.com/awslabs/aws-lambda-powertools-python/issues/459))
* **deps-dev:** bump mkdocs-material from 7.1.6 to 7.1.7 ([#464](https://github.com/awslabs/aws-lambda-powertools-python/issues/464))
* **deps-dev:** bump pytest-cov from 2.12.0 to 2.12.1 ([#454](https://github.com/awslabs/aws-lambda-powertools-python/issues/454))
* **mergify:** use job name to match GH Actions
* **mergify:** disable check for matrix jobs


<a name="v1.16.1"></a>
## [v1.16.1] - 2021-05-23
## Features

* **parser:** security issue in Pydantic [#436](https://github.com/awslabs/aws-lambda-powertools-python/issues/436) ([#437](https://github.com/awslabs/aws-lambda-powertools-python/issues/437))

## Maintenance

* bump to 1.16.1


<a name="v1.16.0"></a>
## [v1.16.0] - 2021-05-17
## Features

* **data-classes:** decode base64 encoded body ([#425](https://github.com/awslabs/aws-lambda-powertools-python/issues/425))
* **data-classes:** support for code pipeline job event ([#416](https://github.com/awslabs/aws-lambda-powertools-python/issues/416))

## Maintenance

* bump to 1.16.0


<a name="v1.15.1"></a>
## [v1.15.1] - 2021-05-13
## Bug Fixes

* **docs:** Use updated names for ProxyEventType ([#424](https://github.com/awslabs/aws-lambda-powertools-python/issues/424))

## Documentation

* update list of features
* **event_handler:** add missing note on trimmed responses

## Maintenance

* bump to 1.15.1


<a name="v1.15.0"></a>
## [v1.15.0] - 2021-05-06
## Bug Fixes

* **deps:** Bump aws-xray-sdk from 2.6.0 to 2.8.0 ([#413](https://github.com/awslabs/aws-lambda-powertools-python/issues/413))
* **docs:** workflow to include api ref in latest alias ([#408](https://github.com/awslabs/aws-lambda-powertools-python/issues/408))
* **parser:** Improve types for parser.py ([#419](https://github.com/awslabs/aws-lambda-powertools-python/issues/419))
* **validator:** event type annotation as any in validate fn ([#405](https://github.com/awslabs/aws-lambda-powertools-python/issues/405))

## Code Refactoring

* simplify custom formatter for minor changes ([#417](https://github.com/awslabs/aws-lambda-powertools-python/issues/417))
* **event-handler:** api gateway handler review changes ([#420](https://github.com/awslabs/aws-lambda-powertools-python/issues/420))
* **event-handler:** Add ResponseBuilder and more docs ([#412](https://github.com/awslabs/aws-lambda-powertools-python/issues/412))
* **logger:** BYOFormatter and Handler, UTC support, and more ([#404](https://github.com/awslabs/aws-lambda-powertools-python/issues/404))

## Documentation

* **api_gateway:** new event handler for API Gateway and ALB ([#418](https://github.com/awslabs/aws-lambda-powertools-python/issues/418))
* **event_handler:** fix closing brackets in CORS sample
* **event_handler:** remove beta flag from new HTTP utility
* **idempotency:** remove beta flag
* **logger:** improvements extensibility & new features ([#415](https://github.com/awslabs/aws-lambda-powertools-python/issues/415))
* **parser:** fix table and heading syntax
* **tracer:** Fix line highlighting ([#395](https://github.com/awslabs/aws-lambda-powertools-python/issues/395))

## Features

* add support to persist default dimensions ([#410](https://github.com/awslabs/aws-lambda-powertools-python/issues/410))
* **event-handle:** allow for cors=None setting ([#421](https://github.com/awslabs/aws-lambda-powertools-python/issues/421))
* **event-handler:** add http ProxyEvent handler ([#369](https://github.com/awslabs/aws-lambda-powertools-python/issues/369))
* **parser:** Support for API GW v1 proxy schema & envelope ([#403](https://github.com/awslabs/aws-lambda-powertools-python/issues/403))

## Maintenance

* bump to 1.15.0 ([#422](https://github.com/awslabs/aws-lambda-powertools-python/issues/422))


<a name="v1.14.0"></a>
## [v1.14.0] - 2021-04-09
## Bug Fixes

* perf tests for Logger and fail str msgs
* downgrade poetry to 1.1.4 ([#385](https://github.com/awslabs/aws-lambda-powertools-python/issues/385))
* lock X-Ray SDK to 2.6.0 ([#384](https://github.com/awslabs/aws-lambda-powertools-python/issues/384))
* **data-classes:** Add missing operationName ([#373](https://github.com/awslabs/aws-lambda-powertools-python/issues/373))
* **idempotent:** Correctly raise IdempotencyKeyError ([#378](https://github.com/awslabs/aws-lambda-powertools-python/issues/378))
* **metrics:** AttributeError raised by MediaManager and Typing and docs ([#357](https://github.com/awslabs/aws-lambda-powertools-python/issues/357))
* **parser:** S3Model support empty keys ([#375](https://github.com/awslabs/aws-lambda-powertools-python/issues/375))
* **tracer:** Correct type hint for MyPy ([#365](https://github.com/awslabs/aws-lambda-powertools-python/issues/365))
* **workflow:** github actions depends on for release

## Documentation

* Fix doc links and line highlights ([#380](https://github.com/awslabs/aws-lambda-powertools-python/issues/380))
* fix extra key for versioning
* update mkdocs-material to 7.1.0
* Correct link targets and line highlights ([#390](https://github.com/awslabs/aws-lambda-powertools-python/issues/390))
* introduce event handlers utility section ([#388](https://github.com/awslabs/aws-lambda-powertools-python/issues/388))
* enable versioning feature ([#374](https://github.com/awslabs/aws-lambda-powertools-python/issues/374))
* **idempotency:** add default configuration for those not using CFN ([#391](https://github.com/awslabs/aws-lambda-powertools-python/issues/391))
* **index:** fix link to event handler
* **logger:** add example on how to set UTC timestamp ([#392](https://github.com/awslabs/aws-lambda-powertools-python/issues/392))
* **validator:** include more complete examples & intro to JSON Schema ([#389](https://github.com/awslabs/aws-lambda-powertools-python/issues/389))

## Features

* **event-handler:** Add AppSync handler decorator ([#363](https://github.com/awslabs/aws-lambda-powertools-python/issues/363))
* **parameter:** add dynamodb_endpoint_url for local_testing ([#376](https://github.com/awslabs/aws-lambda-powertools-python/issues/376))
* **parser:** Add S3 Object Lambda Event ([#362](https://github.com/awslabs/aws-lambda-powertools-python/issues/362))

## Maintenance

* bump to 1.14.0
* add approved by field in RFC template
* make RFC proposal more explicit
* update automated steps in release process


<a name="v1.13.0"></a>
## [v1.13.0] - 2021-03-23
## Bug Fixes

* **deps:** Bump dependencies and fix some of the dev tooling ([#354](https://github.com/awslabs/aws-lambda-powertools-python/issues/354))
* **lint:** Move `tests/THIRD-PARTY-LICENSES` to root ([#352](https://github.com/awslabs/aws-lambda-powertools-python/issues/352))

## Features

* **data-classes:** Add S3 Object Lambda Event ([#353](https://github.com/awslabs/aws-lambda-powertools-python/issues/353))

## Maintenance

* include internals in release template
* bump to 1.13.0
* correct 3rd party license


<a name="v1.12.0"></a>
## [v1.12.0] - 2021-03-17
## Bug Fixes

* **idempotency:** TypeError when calling is_missing_idempotency_key with an int ([#315](https://github.com/awslabs/aws-lambda-powertools-python/issues/315))
* **idempotency:** Correctly handle save_inprogress errors ([#313](https://github.com/awslabs/aws-lambda-powertools-python/issues/313))

## Code Refactoring

* **parameters:** Consistently reference env ([#319](https://github.com/awslabs/aws-lambda-powertools-python/issues/319))

## Documentation

* surface new 1.12.0 features and enhancements  ([#344](https://github.com/awslabs/aws-lambda-powertools-python/issues/344))
* Correct code examples ([#317](https://github.com/awslabs/aws-lambda-powertools-python/issues/317))
* **data-classes:** Add more cognito code examples ([#340](https://github.com/awslabs/aws-lambda-powertools-python/issues/340))
* **idempotency:** Correct examples and line highlights ([#312](https://github.com/awslabs/aws-lambda-powertools-python/issues/312))
* **metrics:** Corrections to the code examples ([#314](https://github.com/awslabs/aws-lambda-powertools-python/issues/314))
* **metrics:** remove minimum dimensions
* **metrics:** Correct code examples in markdown ([#316](https://github.com/awslabs/aws-lambda-powertools-python/issues/316))
* **tracer:** Fix Tracer typing hinting for Pycharm ([#345](https://github.com/awslabs/aws-lambda-powertools-python/issues/345))

## Features

* **data-classes:** Add appsync scalar_types_utils ([#339](https://github.com/awslabs/aws-lambda-powertools-python/issues/339))
* **data-classes:** AppSync Resolver Event ([#323](https://github.com/awslabs/aws-lambda-powertools-python/issues/323))
* **idempotent:** Include function name in the idempotent key ([#326](https://github.com/awslabs/aws-lambda-powertools-python/issues/326))
* **logging:** Add correlation_id support ([#321](https://github.com/awslabs/aws-lambda-powertools-python/issues/321))
* **logging:** Include exception_name ([#320](https://github.com/awslabs/aws-lambda-powertools-python/issues/320))
* **parameters:** Add force_fetch option ([#341](https://github.com/awslabs/aws-lambda-powertools-python/issues/341))

## Maintenance

* bump to 1.12.0
* remove auto-label as restrictions prevent it from working
* increase perf SLA due to slow GitHub Actions machine
* add PR size labelling action # 2
* add PR size labelling action
* add PR auto-label action
* remove gatsby mention as migrated completed


<a name="v1.11.0"></a>
## [v1.11.0] - 2021-03-05
## Bug Fixes

* import time latency by lazily loading high level modules ([#301](https://github.com/awslabs/aws-lambda-powertools-python/issues/301))
* correct behaviour to avoid caching "INPROGRESS" records ([#295](https://github.com/awslabs/aws-lambda-powertools-python/issues/295))
* **idempotency:** PR feedback on config and kwargs

## Code Refactoring

* **idempotent:** Change UX to use a config class for non-persistence related features ([#306](https://github.com/awslabs/aws-lambda-powertools-python/issues/306))
* **metrics:** optimize validation and serialization ([#307](https://github.com/awslabs/aws-lambda-powertools-python/issues/307))

## Documentation

* **batch:** add example on how to integrate with sentry.io ([#308](https://github.com/awslabs/aws-lambda-powertools-python/issues/308))
* **data-classes:** Correct import for DynamoDBRecordEventName ([#299](https://github.com/awslabs/aws-lambda-powertools-python/issues/299))
* **dataclasses:** new Connect Contact Flow ([#310](https://github.com/awslabs/aws-lambda-powertools-python/issues/310))
* **idempotency:** tidy up doc before release ([#309](https://github.com/awslabs/aws-lambda-powertools-python/issues/309))
* **idempotent:** Fix typos and code formatting ([#305](https://github.com/awslabs/aws-lambda-powertools-python/issues/305))

## Features

* Idempotency helper utility ([#245](https://github.com/awslabs/aws-lambda-powertools-python/issues/245))
* **data-classes:** Add connect contact flow event ([#304](https://github.com/awslabs/aws-lambda-powertools-python/issues/304))
* **idempotency:** Add raise_on_no_idempotency_key flag ([#297](https://github.com/awslabs/aws-lambda-powertools-python/issues/297))
* **idempotency:** Fix KeyError when local_cache is True and an error is raised in the lambda handler ([#300](https://github.com/awslabs/aws-lambda-powertools-python/issues/300))
* **idempotent:** Add support for jmespath_options ([#302](https://github.com/awslabs/aws-lambda-powertools-python/issues/302))

## Maintenance

* update changelog ([#311](https://github.com/awslabs/aws-lambda-powertools-python/issues/311))
* adjusts Metrics SLA for slow py36 interpreters
* remove unsuccessful labeler bot
* update labeler bot to sync upon PR changes
* attempt 1 to fix PR labeler


<a name="v1.10.5"></a>
## [v1.10.5] - 2021-02-17
## Maintenance

* version bump to 1.10.5 ([#292](https://github.com/awslabs/aws-lambda-powertools-python/issues/292))


<a name="v1.10.4"></a>
## [v1.10.4] - 2021-02-17
## Bug Fixes

* sync features in main page
* meta tags, and ext link to open in new tab

## Documentation

* **data-classes:** Fix anchor tags to be lower case ([#288](https://github.com/awslabs/aws-lambda-powertools-python/issues/288))

## Maintenance

* version bump to 1.10.4 ([#291](https://github.com/awslabs/aws-lambda-powertools-python/issues/291))
* add default runtime key
* Correct the docs location ([#289](https://github.com/awslabs/aws-lambda-powertools-python/issues/289))
* enable PR labeler workflow
* add auto-label for known files

## Regression

* search input size


<a name="v1.10.3"></a>
## [v1.10.3] - 2021-02-12
## Bug Fixes

* sfix typing hit for envelope parse model ([#286](https://github.com/awslabs/aws-lambda-powertools-python/issues/286))
* disable batching of X-Ray subsegments ([#284](https://github.com/awslabs/aws-lambda-powertools-python/issues/284))

## Documentation

* migrate documentation from Gatsby to MkDocs material ([#279](https://github.com/awslabs/aws-lambda-powertools-python/issues/279))

## Maintenance

* bump to 1.10.3 ([#287](https://github.com/awslabs/aws-lambda-powertools-python/issues/287))


<a name="v1.10.2"></a>
## [v1.10.2] - 2021-02-04
## Bug Fixes

* remove unnecessary typing-extensions for py3.8 ([#281](https://github.com/awslabs/aws-lambda-powertools-python/issues/281))
* batch processing exceptions ([#276](https://github.com/awslabs/aws-lambda-powertools-python/issues/276))

## Documentation

* **appconfig:** Use correct import for docstring ([#271](https://github.com/awslabs/aws-lambda-powertools-python/issues/271))

## Maintenance

* bump to 1.10.2 ([#282](https://github.com/awslabs/aws-lambda-powertools-python/issues/282))
* fix immer and socket.io CVEs ([#278](https://github.com/awslabs/aws-lambda-powertools-python/issues/278))
* typo in parser docs


<a name="v1.10.1"></a>
## [v1.10.1] - 2021-01-19
## Features

* add support for SNS->SQS protocol ([#272](https://github.com/awslabs/aws-lambda-powertools-python/issues/272))

## Maintenance

* bump to 1.10.1 ([#273](https://github.com/awslabs/aws-lambda-powertools-python/issues/273))


<a name="v1.10.0"></a>
## [v1.10.0] - 2021-01-18
## Documentation

* fix import ([#267](https://github.com/awslabs/aws-lambda-powertools-python/issues/267))
* add info about extras layer ([#260](https://github.com/awslabs/aws-lambda-powertools-python/issues/260))
* fix note whitespace
* add missing parser models ([#254](https://github.com/awslabs/aws-lambda-powertools-python/issues/254))

## Features

* toggle to disable log deduplication locally for pytest live log [#262](https://github.com/awslabs/aws-lambda-powertools-python/issues/262) ([#268](https://github.com/awslabs/aws-lambda-powertools-python/issues/268))
* Add AppConfig parameter provider ([#236](https://github.com/awslabs/aws-lambda-powertools-python/issues/236))
* support extra parameter in Logger messages ([#257](https://github.com/awslabs/aws-lambda-powertools-python/issues/257))
* support custom formats in JSON Schema validation ([#247](https://github.com/awslabs/aws-lambda-powertools-python/issues/247))

## Maintenance

* bump to 1.10.0 ([#270](https://github.com/awslabs/aws-lambda-powertools-python/issues/270))
* move env names to constant file ([#264](https://github.com/awslabs/aws-lambda-powertools-python/issues/264))
* update stale bot
* general simplifications and cleanup ([#255](https://github.com/awslabs/aws-lambda-powertools-python/issues/255))
* hardcode axios transitive resolution ([#256](https://github.com/awslabs/aws-lambda-powertools-python/issues/256))


<a name="v1.9.1"></a>
## [v1.9.1] - 2020-12-21
## Bug Fixes

* ensures all Loggers have unique service names

## Code Refactoring

* convert dict into a literal dict object and re-use it

## Documentation

* add clarification to Tracer docs for how `capture_method` decorator can cause function responses to be read and serialized.

## Features

* **pep-561:** Create py.typed file and include into pyproject.

## Maintenance

* bump to 1.9.1 ([#252](https://github.com/awslabs/aws-lambda-powertools-python/issues/252))
* add changelog
* implement phony targets correctly
* **deps:** bump ini from 1.3.5 to 1.3.8 in /docs

## Pull Requests

* Merge pull request [#250](https://github.com/awslabs/aws-lambda-powertools-python/issues/250) from heitorlessa/fix/[#249](https://github.com/awslabs/aws-lambda-powertools-python/issues/249)
* Merge pull request [#235](https://github.com/awslabs/aws-lambda-powertools-python/issues/235) from Nr18/phony
* Merge pull request [#244](https://github.com/awslabs/aws-lambda-powertools-python/issues/244) from awslabs/docs/capture_method_clarification
* Merge pull request [#241](https://github.com/awslabs/aws-lambda-powertools-python/issues/241) from awslabs/dependabot/npm_and_yarn/docs/ini-1.3.8
* Merge pull request [#237](https://github.com/awslabs/aws-lambda-powertools-python/issues/237) from gmcrocetti/pep-561
* Merge pull request [#234](https://github.com/awslabs/aws-lambda-powertools-python/issues/234) from Nr18/test-equal
* Merge pull request [#233](https://github.com/awslabs/aws-lambda-powertools-python/issues/233) from GroovyDan/improv/add_equality_check_to_dict_wrapper
* Merge pull request [#232](https://github.com/awslabs/aws-lambda-powertools-python/issues/232) from gyft/add-missing-tests


<a name="v1.9.0"></a>
## [v1.9.0] - 2020-12-04
## Bug Fixes

* s3 model import
* cloudwatch logs envelope typo

## Documentation

* add Kinesis Streams as a supported model & envelope
* add S3 as a supported model
* add CW Logs as a supported envelope
* add CW Logs as a supported model
* add Alb as a supported model
* shadow sidebar to remain expanded
* add source code link in nav bar
* fix broken link for github

## Features

* Add Kinesis lambda event support to Parser utility
* Add cloudwatch lambda event support to Parser utility
* Add alb lambda event support to Parser utility [#228](https://github.com/awslabs/aws-lambda-powertools-python/issues/228)
* Add Kinesis lambda event support to Parser utility
* Add S3 lambda event support to Parser utility [#224](https://github.com/awslabs/aws-lambda-powertools-python/issues/224)
* Add Ses lambda event support to Parser utility [#213](https://github.com/awslabs/aws-lambda-powertools-python/issues/213)

## Maintenance

* bump version to 1.9.0

## Pull Requests

* Merge pull request [#227](https://github.com/awslabs/aws-lambda-powertools-python/issues/227) from risenberg-cyberark/kinesis
* Merge pull request [#225](https://github.com/awslabs/aws-lambda-powertools-python/issues/225) from risenberg-cyberark/s3
* Merge pull request [#231](https://github.com/awslabs/aws-lambda-powertools-python/issues/231) from risenberg-cyberark/cloudwatch
* Merge pull request [#229](https://github.com/awslabs/aws-lambda-powertools-python/issues/229) from risenberg-cyberark/alb
* Merge pull request [#223](https://github.com/awslabs/aws-lambda-powertools-python/issues/223) from heitorlessa/docs/add-source-code-link
* Merge pull request [#222](https://github.com/awslabs/aws-lambda-powertools-python/issues/222) from awslabs/docs-fix-broken-link
* Merge pull request [#219](https://github.com/awslabs/aws-lambda-powertools-python/issues/219) from igorlg/docs/logger-supress-clarify
* Merge pull request [#214](https://github.com/awslabs/aws-lambda-powertools-python/issues/214) from risenberg-cyberark/ses


<a name="v1.8.0"></a>
## [v1.8.0] - 2020-11-20
## Bug Fixes

* replace now deprecated set-env with new GitHub Env file
* remove dummy heading to prevent htmlAst bug

## Documentation

* correct example usage of SES data class
* add faq section
* add minimal permission set for using layer

## Features

* include new replay-name field in parser and data_classes
* **data_classes:** API Gateway V2 IAM and Lambda

## Maintenance

* bump to 1.8.0
* bump dependencies
* **docs:** Add some of the missing docstrings

## Pull Requests

* Merge pull request [#212](https://github.com/awslabs/aws-lambda-powertools-python/issues/212) from heitorlessa/chore/bump-1.8.0
* Merge pull request [#211](https://github.com/awslabs/aws-lambda-powertools-python/issues/211) from heitorlessa/feat/eventbridge-replay-support
* Merge pull request [#209](https://github.com/awslabs/aws-lambda-powertools-python/issues/209) from awslabs/docs/correct_ses_dataclass_example
* Merge pull request [#207](https://github.com/awslabs/aws-lambda-powertools-python/issues/207) from risenberg-cyberark/sns
* Merge pull request [#205](https://github.com/awslabs/aws-lambda-powertools-python/issues/205) from heitorlessa/chore/update-docs-dep
* Merge pull request [#202](https://github.com/awslabs/aws-lambda-powertools-python/issues/202) from Nr18/logger-faq
* Merge pull request [#204](https://github.com/awslabs/aws-lambda-powertools-python/issues/204) from am29d/docs/add-iam-permissions-for-layer
* Merge pull request [#201](https://github.com/awslabs/aws-lambda-powertools-python/issues/201) from gyft/feat-data-classes-event-updates


<a name="v1.7.0"></a>
## [v1.7.0] - 2020-10-26
## Bug Fixes

* _parse return type
* high and security peer dependency vulnerabilities
* change to Yarn to support manual resolutions
* generic type to match ABC bound class
* debug logging in envelopes before each parsing
* remove malformed 3.1. sentence
* ensures parser can take json strings as input
* parse high level import
* code inspect issues
* unnecessary return; better error handling
* snake_case
* comment out validators [#118](https://github.com/awslabs/aws-lambda-powertools-python/issues/118)
* CR fixes Merge branch 'develop' of https://github.com/awslabs/aws-lambda-powertools-python into pydantic
* reduce complexity of dynamo envelope
* poetry update + pydantic, typing_extensions as optional
* add only pydantic (+1 squashed commit) Squashed commits: [804f251] fix poetry.lock, revert changes
* Correct typo
* remove only dev extras
* remove jmespath extras in Make

## Code Refactoring

* pydantic as optional dependancy, remove lambdaContext
* change to advanced parser

## Documentation

* reorder parser's payload sample position
* add more info on conditional keys [#195](https://github.com/awslabs/aws-lambda-powertools-python/issues/195)
* add a note that decorator will replace the event
* address Ran's feedback
* reorder data validation; improve envelopes section
* reorder extending models as parse fn wasn't introduced
* use yarn's resolution to fix incompatible dependency
* add cold start data
* add a FAQ section
* ensure examples can be copied/pasted as-is
* add extending built-in models
* add envelope section
* add data model validation section
* use non-hello world model to better exemplify parsing
* add 101 parsing events content
* initial structure for parser docs
* initial sketch of parser docs
* update examples in README

## Features

* experiment with codeQL over LGTM
* add standalone parse function
* Advanced parser utility (pydantic)
* RFC: Validate incoming and outgoing events utility [#95](https://github.com/awslabs/aws-lambda-powertools-python/issues/95)
* **data_classes:** case insensitive header lookup
* **data_classes:** Cognito custom auth triggers

## Maintenance

* fix repository URL
* bump version to 1.7.0
* spacing
* typo in list
* typo on code generation tool
* remove flake8 polyfill as explicit dep
* explicit DynamoDB Stream schema naming
* lint
* kwarg over arg to ease refactoring
* remove test for commented code
* fix make build syntax for internal build whl
* upgrade docs dep
* remove dev deps from example project
* remove kitchen sink example
* upgrade gatsby
* upgrade amplify, antd, and gatsby plugins
* upgrade apollo-docs theme
* remove dev deps from example project
* remove kitchen sink example

## Reverts
* fix: remove jmespath extras in Make
* fix: remove jmespath extras in Make

## Pull Requests

* Merge pull request [#200](https://github.com/awslabs/aws-lambda-powertools-python/issues/200) from heitorlessa/chore/bump-1.7.0
* Merge pull request [#199](https://github.com/awslabs/aws-lambda-powertools-python/issues/199) from heitorlessa/docs/clarify-dynamic-log-keys
* Merge pull request [#198](https://github.com/awslabs/aws-lambda-powertools-python/issues/198) from awslabs/improv/suppress-logger-propagation
* Merge pull request [#192](https://github.com/awslabs/aws-lambda-powertools-python/issues/192) from heitorlessa/docs/parser
* Merge pull request [#196](https://github.com/awslabs/aws-lambda-powertools-python/issues/196) from awslabs/dependabot/npm_and_yarn/docs/object-path-0.11.5
* Merge pull request [#189](https://github.com/awslabs/aws-lambda-powertools-python/issues/189) from heitorlessa/improv/parser[#118](https://github.com/awslabs/aws-lambda-powertools-python/issues/118)
* Merge pull request [#186](https://github.com/awslabs/aws-lambda-powertools-python/issues/186) from gyft/feat-case-insensitive-dict
* Merge pull request [#188](https://github.com/awslabs/aws-lambda-powertools-python/issues/188) from gyft/tests-pydantic
* Merge pull request [#178](https://github.com/awslabs/aws-lambda-powertools-python/issues/178) from gyft/cognito-custom-auth
* Merge pull request [#118](https://github.com/awslabs/aws-lambda-powertools-python/issues/118) from risenberg-cyberark/pydantic
* Merge pull request [#181](https://github.com/awslabs/aws-lambda-powertools-python/issues/181) from awslabs/fix/docs-sec-vuln
* Merge pull request [#180](https://github.com/awslabs/aws-lambda-powertools-python/issues/180) from heitorlessa/chore/remove-example


<a name="v1.6.1"></a>
## [v1.6.1] - 2020-09-23
## Maintenance

* bump to 1.6.1 ([#177](https://github.com/awslabs/aws-lambda-powertools-python/issues/177))


<a name="v1.6.0"></a>
## [v1.6.0] - 2020-09-22
## Bug Fixes

* apply Tom's suggestion
* branding
* Correct description for data classes util
* duplicate features content
* navigation, branding
* remove DeleteMessageBatch call to SQS api if there are no messages to delete ([#170](https://github.com/awslabs/aws-lambda-powertools-python/issues/170))
* correct type hint Dict instead of dict

## Code Refactoring

* correct type hint

## Documentation

* fixed more typos, correct index reference to new util
* fix typo in DynamoDB example
* add docs for data classes utility
* improve wording on jmespath fns
* document validator utility

## Features

* add custom jmespath functions support
* emf multiple metric values ([#167](https://github.com/awslabs/aws-lambda-powertools-python/issues/167))
* add initial validator tests
* add cloudwatch_logs based on Bryan's feedback
* add powertools_base64 custom fn
* add built-in envelopes
* add jmespath as optional dependency
* add initial draft simple validator
* **trigger:** data class and helper functions for lambda trigger events ([#159](https://github.com/awslabs/aws-lambda-powertools-python/issues/159))

## Maintenance

* typo
* bump to 1.6.0
* better type hinting
* update changelog
* fix docstring; import order

## Pull Requests

* Merge pull request [#175](https://github.com/awslabs/aws-lambda-powertools-python/issues/175) from heitorlessa/chore/bump-1.6.0
* Merge pull request [#171](https://github.com/awslabs/aws-lambda-powertools-python/issues/171) from awslabs/docs/data_classes
* Merge pull request [#174](https://github.com/awslabs/aws-lambda-powertools-python/issues/174) from heitorlessa/improv/docs-logger-metrics-testing
* Merge pull request [#168](https://github.com/awslabs/aws-lambda-powertools-python/issues/168) from gyft/tests-missing
* Merge pull request [#153](https://github.com/awslabs/aws-lambda-powertools-python/issues/153) from heitorlessa/feat/validator-utility


<a name="v1.5.0"></a>
## [v1.5.0] - 2020-09-04
## Bug Fixes

* throw exception by default if messages processing fails
* add sqs_batch_processor as its own method
* ensure debug log event has latest ctx
* update image with correct sample
* ensures xray_trace_id is refreshed
* typo in example
* include proposed suggestions
* **base-partial:** append record instead of entry
* **logging:** Don't include `json_default` in logs ([#132](https://github.com/awslabs/aws-lambda-powertools-python/issues/132))

## Code Refactoring

* changes partial_sqs middleware in favor of a generic interface always expecting a BatchProcessor
* replace LambdaEvent with Dict[str, Any]
* remove initial reference
* fix import issues and provide context in docblocks
* split properties and add docblocks
* split the objects into seperate files
* make requested changes
* use None instead of
* batch middleware
* remove references to BaseProcessor. Left BasePartialProcessor
* change return for failure/success handlers
* **sqs:** add module middlewares
* **sqs:** change methods to protected
* **tests:** update tests to new batch processor middleware
* **tests:** processor using default config

## Documentation

* address readability feedbacks
* add detail to batch processing
* simplify documentation more SQS specific focus Update for sqs_batch_processor interface
* rephrase the wording to make it more clear
* refactor example; improve docs about creating your own processor
* add newly created Slack Channel
* describe the typing utility
* add troubleshooting section
* add xray_trace_id key
* fix suggestions made by [@heitorlessa](https://github.com/heitorlessa)
* add description where to find the layer arn ([#145](https://github.com/awslabs/aws-lambda-powertools-python/issues/145))
* new section "Migrating from other Loggers" ([#148](https://github.com/awslabs/aws-lambda-powertools-python/issues/148))
* minor edit to letter case part 2
* user specific documentation
* Fix doc for log sampling ([#135](https://github.com/awslabs/aws-lambda-powertools-python/issues/135))
* **partial-processor:** add simple docstrings to success/failure handlers
* **sqs:** docstrings for PartialSQS
* **sqs-base:** docstring for base class

## Features

* add xray_trace_id key when tracing is active [#137](https://github.com/awslabs/aws-lambda-powertools-python/issues/137)
* initial implementation as the proposed gist is
* add sqs failure processors
* include base processors
* add batch module
* add package level import for batch utility
* **logger:** readable log_dict seq
* **logging:** suppress some log keys
* **logging:** allow for custom json order
* **parameters:** transform = "auto" ([#133](https://github.com/awslabs/aws-lambda-powertools-python/issues/133))
* **sqs:** add optional config parameter
* **sqs:** improve validation for queue_url

## Maintenance

* bump version to 1.5.0 ([#158](https://github.com/awslabs/aws-lambda-powertools-python/issues/158))
* tiny changes for readability
* add debug logging for sqs batch processing
* remove middlewares module, moving decorator functionality to base and sqs
* add test for sqs_batch_processor interface
* add sqs_batch_processor decorator to simplify interface
* fix typos, docstrings and type hints ([#154](https://github.com/awslabs/aws-lambda-powertools-python/issues/154))
* doc typo
* **batch:** Housekeeping for recent changes ([#157](https://github.com/awslabs/aws-lambda-powertools-python/issues/157))

## Pull Requests

* Merge pull request [#149](https://github.com/awslabs/aws-lambda-powertools-python/issues/149) from Nr18/static-types
* Merge pull request [#155](https://github.com/awslabs/aws-lambda-powertools-python/issues/155) from awslabs/docs/batch_processing_util
* Merge pull request [#100](https://github.com/awslabs/aws-lambda-powertools-python/issues/100) from gmcrocetti/partial-sqs-batch
* Merge pull request [#151](https://github.com/awslabs/aws-lambda-powertools-python/issues/151) from Nr18/troubleshooting
* Merge pull request [#150](https://github.com/awslabs/aws-lambda-powertools-python/issues/150) from heitorlessa/feat/logger-add-xray-trace-id
* Merge pull request [#140](https://github.com/awslabs/aws-lambda-powertools-python/issues/140) from gyft/fix-log-key-order
* Merge pull request [#142](https://github.com/awslabs/aws-lambda-powertools-python/issues/142) from gyft/fix-letter-case


<a name="v1.4.0"></a>
## [v1.4.0] - 2020-08-25
## Bug Fixes

* upgrade dot-prop, serialize-javascript
* remove actual response from debug logs
* naming and staticmethod consistency
* correct in_subsegment assertion
* update cold_start doc to reflect [#125](https://github.com/awslabs/aws-lambda-powertools-python/issues/125)
* split ColdStart metric to its own EMF blob [#125](https://github.com/awslabs/aws-lambda-powertools-python/issues/125)
* **ssm:** Make decrypt an explicit option and refactoring ([#123](https://github.com/awslabs/aws-lambda-powertools-python/issues/123))

## Documentation

* add Lambda Layer SAR App url and ARN
* move tenets; remove extra space
* use table for clarity
* add blog post, and quick example
* subtle rewording for better clarity
* fix typos, log_event & sampling wording
* make sensitive info more explicit with an example
* create Patching modules section; cleanup response wording
* move concurrent asynchronous under escape hatch
* grammar
* bring new feature upfront when returning sensitive info

## Features

* capture_response as metadata option [#127](https://github.com/awslabs/aws-lambda-powertools-python/issues/127)

## Maintenance

* bump to 1.4.0
* update internal docstrings for consistency
* update changelog to reflect new feature
* clarify changelog bugfix vs breaking change
* remove/correct unnecessary debug logs
* fix debug log adding unused obj
* grammar
* add metrics fix description
* correct typos

## Pull Requests

* Merge pull request [#129](https://github.com/awslabs/aws-lambda-powertools-python/issues/129) from am29d/feat/lambda-layers
* Merge pull request [#130](https://github.com/awslabs/aws-lambda-powertools-python/issues/130) from heitorlessa/docs/readability-improvements
* Merge pull request [#128](https://github.com/awslabs/aws-lambda-powertools-python/issues/128) from heitorlessa/feat/tracer-disallow-response-metadata
* Merge pull request [#126](https://github.com/awslabs/aws-lambda-powertools-python/issues/126) from heitorlessa/fix/metrics-cold-start-split


<a name="v1.3.1"></a>
## [v1.3.1] - 2020-08-22
## Bug Fixes

* **capture_method:** should yield inside with ([#124](https://github.com/awslabs/aws-lambda-powertools-python/issues/124))

## Maintenance

* version bump to 1.3.1
* **deps:** bump prismjs from 1.20.0 to 1.21.0 in /docs
* **deps:** bump elliptic from 6.5.2 to 6.5.3 in /docs

## Pull Requests

* Merge pull request [#120](https://github.com/awslabs/aws-lambda-powertools-python/issues/120) from awslabs/dependabot/npm_and_yarn/docs/elliptic-6.5.3
* Merge pull request [#121](https://github.com/awslabs/aws-lambda-powertools-python/issues/121) from awslabs/dependabot/npm_and_yarn/docs/prismjs-1.21.0


<a name="v1.3.0"></a>
## [v1.3.0] - 2020-08-21
## Features

* add parameter utility ([#96](https://github.com/awslabs/aws-lambda-powertools-python/issues/96))

## Maintenance

* bump version to 1.3.0 ([#122](https://github.com/awslabs/aws-lambda-powertools-python/issues/122))


<a name="v1.2.0"></a>
## [v1.2.0] - 2020-08-20
## Features

* add support for tracing of generators using capture_method decorator ([#113](https://github.com/awslabs/aws-lambda-powertools-python/issues/113))

## Maintenance

* bump version to 1.2.0 ([#119](https://github.com/awslabs/aws-lambda-powertools-python/issues/119))


<a name="v1.1.3"></a>
## [v1.1.3] - 2020-08-18
## Bug Fixes

* remove root logger handler set by Lambda [#115](https://github.com/awslabs/aws-lambda-powertools-python/issues/115)

## Maintenance

* bump to 1.1.3

## Pull Requests

* Merge pull request [#117](https://github.com/awslabs/aws-lambda-powertools-python/issues/117) from heitorlessa/chore/bump-1.1.3
* Merge pull request [#116](https://github.com/awslabs/aws-lambda-powertools-python/issues/116) from heitorlessa/fix/remove-root-logger-handler


<a name="v1.1.2"></a>
## [v1.1.2] - 2020-08-16
## Bug Fixes

* return subclass [#107](https://github.com/awslabs/aws-lambda-powertools-python/issues/107)

## Documentation

* clarify auto_patch as per [#108](https://github.com/awslabs/aws-lambda-powertools-python/issues/108)

## Maintenance

* bump version to 1.1.2
* suppress LGTM alert
* add autocomplete as unreleased
* remove unused stdout fixture
* update Tracer docs as per [#108](https://github.com/awslabs/aws-lambda-powertools-python/issues/108)

## Pull Requests

* Merge pull request [#111](https://github.com/awslabs/aws-lambda-powertools-python/issues/111) from heitorlessa/chore/bump-1.1.2
* Merge pull request [#110](https://github.com/awslabs/aws-lambda-powertools-python/issues/110) from heitorlessa/improv/logger-auto-complete
* Merge pull request [#109](https://github.com/awslabs/aws-lambda-powertools-python/issues/109) from heitorlessa/docs/tracer-reuse


<a name="v1.1.1"></a>
## [v1.1.1] - 2020-08-14
## Bug Fixes

* regression 104 ([#105](https://github.com/awslabs/aws-lambda-powertools-python/issues/105))
* return log level int immediately
* add test covering logging constant

## Maintenance

* bump patch version
* fix unused fixture
* fix docstring on level [str,int] consistency
* fix test level typo
* trigger docs on new release ([#102](https://github.com/awslabs/aws-lambda-powertools-python/issues/102)) ([#103](https://github.com/awslabs/aws-lambda-powertools-python/issues/103))
* trigger docs on new release ([#102](https://github.com/awslabs/aws-lambda-powertools-python/issues/102))
* trigger docs on new release

## Regression

* log level docstring as str

## Pull Requests

* Merge pull request [#106](https://github.com/awslabs/aws-lambda-powertools-python/issues/106) from heitorlessa/fix/regression-104


<a name="v1.1.0"></a>
## [v1.1.0] - 2020-08-14
## Bug Fixes

* auto-assigner filename as per docs

## Features

* add support for logger inheritance ([#99](https://github.com/awslabs/aws-lambda-powertools-python/issues/99))
* enable issue auto-assigner to core team

## Maintenance

* bump to 1.1.0 ([#101](https://github.com/awslabs/aws-lambda-powertools-python/issues/101))
* **deps:** bump lodash from 4.17.15 to 4.17.19 in /docs ([#93](https://github.com/awslabs/aws-lambda-powertools-python/issues/93))


<a name="v1.0.2"></a>
## [v1.0.2] - 2020-07-16
## Maintenance

* bump to 1.0.2 ([#90](https://github.com/awslabs/aws-lambda-powertools-python/issues/90))
* support aws-xray-sdk >=2.5.0 till <3.0.0 ([#89](https://github.com/awslabs/aws-lambda-powertools-python/issues/89))


<a name="v1.0.1"></a>
## [v1.0.1] - 2020-07-05
## Bug Fixes

* append structured logs when injecting lambda context  ([#86](https://github.com/awslabs/aws-lambda-powertools-python/issues/86))

## Documentation

* add blog post in the readme


<a name="v1.0.0"></a>
## [v1.0.0] - 2020-06-18
## Documentation

* customize contributing guide ([#77](https://github.com/awslabs/aws-lambda-powertools-python/issues/77))

## Features

* docs anonymized page view ([#82](https://github.com/awslabs/aws-lambda-powertools-python/issues/82))
* add metrics metadata ([#81](https://github.com/awslabs/aws-lambda-powertools-python/issues/81))

## Maintenance

* bump to 1.0.0 GA ([#83](https://github.com/awslabs/aws-lambda-powertools-python/issues/83))
* add missing ':' and identation in examples
* cleanup tests ([#79](https://github.com/awslabs/aws-lambda-powertools-python/issues/79))
* remove deprecated code before GA ([#78](https://github.com/awslabs/aws-lambda-powertools-python/issues/78))
* move blockquotes as hidden comments


<a name="v0.11.0"></a>
## [v0.11.0] - 2020-06-10
## Bug Fixes

* default dimension creation now happens when metrics are serialized instead of on metrics constructor ([#74](https://github.com/awslabs/aws-lambda-powertools-python/issues/74))

## Maintenance

* update CHANGELOG
* bump version to 0.11.0 ([#76](https://github.com/awslabs/aws-lambda-powertools-python/issues/76))


<a name="v0.10.1"></a>
## [v0.10.1] - 2020-06-10
## Bug Fixes

* default dimension creation now happens when metrics are serialized instead of on metrics constructor ([#74](https://github.com/awslabs/aws-lambda-powertools-python/issues/74))

## Documentation

* fix contrast on highlighted code text ([#73](https://github.com/awslabs/aws-lambda-powertools-python/issues/73))

## Features

* improve error handling for log_metrics decorator ([#71](https://github.com/awslabs/aws-lambda-powertools-python/issues/71))
* add high level imports ([#70](https://github.com/awslabs/aws-lambda-powertools-python/issues/70))

## Maintenance

* version bump 0.10.1
* **deps:** bump graphql-playground-html from 1.6.19 to 1.6.25 in /docs

## Pull Requests

* Merge pull request [#72](https://github.com/awslabs/aws-lambda-powertools-python/issues/72) from awslabs/dependabot/npm_and_yarn/docs/graphql-playground-html-1.6.25


<a name="v0.10.0"></a>
## v0.10.0 - 2020-06-08
## Bug Fixes

* correct env var name for publish to pypi test ([#69](https://github.com/awslabs/aws-lambda-powertools-python/issues/69))
* release-drafter action syntax
* release-drafter label for new feature/major non-breaking changes
* cast dimension value to str to avoid issue where EMF silently fails ([#52](https://github.com/awslabs/aws-lambda-powertools-python/issues/52))
* ignore path that might seem a broken link [#49](https://github.com/awslabs/aws-lambda-powertools-python/issues/49)
* open api ref in a new tab [#48](https://github.com/awslabs/aws-lambda-powertools-python/issues/48)
* metrics not being flushed on every invocation ([#45](https://github.com/awslabs/aws-lambda-powertools-python/issues/45))
* [#35](https://github.com/awslabs/aws-lambda-powertools-python/issues/35) duplicate changelog to project root
* [#24](https://github.com/awslabs/aws-lambda-powertools-python/issues/24) correct example test and docs
* CI attempt 4
* CI attempt 3
* CI attempt 3
* CI attempt 2
* add missing single_metric example; test var name
* fix import of aws_lambda_logging to relative import
* **Makefile:** format before linting
* **make:** add twine as a dev dep
* **setup:** correct invalid license classifier
* **setup:** correct license to MIT-0 in meta

## Documentation

* build on master only
* clarify logger debug sampling message
* clean up readme in favour of docs website
* add install in main docs website
* add pypi badge

## Features

* add capture_cold_start_metric for log_metrics ([#67](https://github.com/awslabs/aws-lambda-powertools-python/issues/67))
* automate publishing to pypi ([#58](https://github.com/awslabs/aws-lambda-powertools-python/issues/58))
* add pre-commit hooks ([#64](https://github.com/awslabs/aws-lambda-powertools-python/issues/64))
* update Metrics interface to resemble tracer & logger: use "service" as its namespace.
* add codecov service ([#59](https://github.com/awslabs/aws-lambda-powertools-python/issues/59))
* add security and complexity baseline [#33](https://github.com/awslabs/aws-lambda-powertools-python/issues/33) ([#57](https://github.com/awslabs/aws-lambda-powertools-python/issues/57))
* add pull request template [#33](https://github.com/awslabs/aws-lambda-powertools-python/issues/33)
* add RFC template for proposals
* create issue templates
* readd release drafter action [#33](https://github.com/awslabs/aws-lambda-powertools-python/issues/33)
* add release drafter ([#56](https://github.com/awslabs/aws-lambda-powertools-python/issues/56))
* add stale issues config [#33](https://github.com/awslabs/aws-lambda-powertools-python/issues/33) ([#55](https://github.com/awslabs/aws-lambda-powertools-python/issues/55))
* enforce semantic PR titles ([#54](https://github.com/awslabs/aws-lambda-powertools-python/issues/54))
* add algolia search for docs and api ref ([#39](https://github.com/awslabs/aws-lambda-powertools-python/issues/39))
* add documentation website ([#37](https://github.com/awslabs/aws-lambda-powertools-python/issues/37))
* add docs to CI
* Add Python3.8 support
* **logger:** add log sampling
* **pypi:** add bumpversion, public release pypi
* **pyproject.toml:** move to poetry

## Maintenance

* version bump ([#68](https://github.com/awslabs/aws-lambda-powertools-python/issues/68))
* public beta version
* rename Makefile target docs-dev to docs-local ([#65](https://github.com/awslabs/aws-lambda-powertools-python/issues/65))
* correct docstring for log_metrics
* fix typo in metrics doc
* Correct test comment
* remove unused import
* formatting
* plat wheels are not needed
* reformat changelog to follow KeepAChangelog standard ([#50](https://github.com/awslabs/aws-lambda-powertools-python/issues/50))
* bump to release candidate
* renamed history to changelog dependabot
* grammar issues
* bump example to use 0.8.0 features
* clean up CI workflows
* fix github badge typo
* pypi monthly download badge
* lint
* bump 0.3.1 with logging patch
* bump history
* lint
* add Python 3.8 in badge as it's supported
* CI badge
* public beta version
* **deps:** bump bleach from 3.1.0 to 3.1.1 in /python
* **deps:** bump websocket-extensions from 0.1.3 to 0.1.4 in /docs ([#66](https://github.com/awslabs/aws-lambda-powertools-python/issues/66))

## Pull Requests

* Merge pull request [#60](https://github.com/awslabs/aws-lambda-powertools-python/issues/60) from awslabs/improv/metrics_interface
* Merge pull request [#8](https://github.com/awslabs/aws-lambda-powertools-python/issues/8) from awslabs/dependabot/pip/python/bleach-3.1.1
* Merge pull request [#7](https://github.com/awslabs/aws-lambda-powertools-python/issues/7) from danilohgds/sampling_feature
* Merge pull request [#5](https://github.com/awslabs/aws-lambda-powertools-python/issues/5) from jfuss/feat/python38


[Unreleased]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v1.24.2...HEAD
[v1.24.2]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v1.24.1...v1.24.2
[v1.24.1]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v1.24.0...v1.24.1
[v1.24.0]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v1.23.0...v1.24.0
[v1.23.0]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v1.22.0...v1.23.0
[v1.22.0]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v1.21.1...v1.22.0
[v1.21.1]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v1.21.0...v1.21.1
[v1.21.0]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v1.20.2...v1.21.0
[v1.20.2]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v1.20.1...v1.20.2
[v1.20.1]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v1.20.0...v1.20.1
[v1.20.0]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v1.19.0...v1.20.0
[v1.19.0]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v1.18.1...v1.19.0
[v1.18.1]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v1.18.0...v1.18.1
[v1.18.0]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v1.17.1...v1.18.0
[v1.17.1]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v1.17.0...v1.17.1
[v1.17.0]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v1.16.1...v1.17.0
[v1.16.1]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v1.16.0...v1.16.1
[v1.16.0]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v1.15.1...v1.16.0
[v1.15.1]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v1.15.0...v1.15.1
[v1.15.0]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v1.14.0...v1.15.0
[v1.14.0]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v1.13.0...v1.14.0
[v1.13.0]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v1.12.0...v1.13.0
[v1.12.0]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v1.11.0...v1.12.0
[v1.11.0]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v1.10.5...v1.11.0
[v1.10.5]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v1.10.4...v1.10.5
[v1.10.4]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v1.10.3...v1.10.4
[v1.10.3]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v1.10.2...v1.10.3
[v1.10.2]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v1.10.1...v1.10.2
[v1.10.1]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v1.10.0...v1.10.1
[v1.10.0]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v1.9.1...v1.10.0
[v1.9.1]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v1.9.0...v1.9.1
[v1.9.0]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v1.8.0...v1.9.0
[v1.8.0]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v1.7.0...v1.8.0
[v1.7.0]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v1.6.1...v1.7.0
[v1.6.1]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v1.6.0...v1.6.1
[v1.6.0]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v1.5.0...v1.6.0
[v1.5.0]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v1.4.0...v1.5.0
[v1.4.0]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v1.3.1...v1.4.0
[v1.3.1]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v1.3.0...v1.3.1
[v1.3.0]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v1.2.0...v1.3.0
[v1.2.0]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v1.1.3...v1.2.0
[v1.1.3]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v1.1.2...v1.1.3
[v1.1.2]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v1.1.1...v1.1.2
[v1.1.1]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v1.1.0...v1.1.1
[v1.1.0]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v1.0.2...v1.1.0
[v1.0.2]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v1.0.1...v1.0.2
[v1.0.1]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v1.0.0...v1.0.1
[v1.0.0]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v0.11.0...v1.0.0
[v0.11.0]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v0.10.1...v0.11.0
[v0.10.1]: https://github.com/awslabs/aws-lambda-powertools-python/compare/v0.10.0...v0.10.1
