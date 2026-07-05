# CAP 认知差错与正确认知框架报告

> Status: analysis · Non-normative · Date: 2026-07-05

## 执行摘要

这次偏差不是“CAP 方向没有价值”，而是我们把两个层级不同的问题放进了同一个概念里：

1. 现有 `cap-docs` 实际定义的是一个**上下文摘要与安全读对象协议**。它的核心链路是：

   ```text
   source object -> field catalog -> context digest -> model response -> gated follow-up
   ```

2. 深度研究报告要求的 CAP 是一个更大的**机器可操作研究对象装配协议**。它要把语义对象、执行能力、运行环境、资源约束、外部服务、授权决策和运行证据装配成可发现、可执行、可审计的契约。

认知差错在于：我们把一个有价值的**局部机制**误认为足以承担整个**跨层协议**。现有方案适合作为 CAP 生态中的 `CAP-Digest` 或 `Context Digest Profile`，但不应直接被称为完整的 CAP Core。

正确框架应当是分层的：

```text
CAP-Core
  研究对象图、Capability、Runtime、ResourceBinding、ServiceBinding、
  Policy、Run、Evidence、Profile、Binding

CAP-Digest
  SourceRef、Field、Digest、DigestManifest、Caveat、Follow-up Gate

External Standards
  MCP、Skills、CWL、RO-Crate、OCI、WASI、Kubernetes、REAPI、
  Sigstore、in-toto、SPDX、CycloneDX、OPA/Cedar
```

当前文档不应被废弃，而应被降级和重命名为 CAP 的上下文证据层。

## 对照依据

本报告基于两个材料之间的差异分析：

- 当前 `cap-docs`：以 `context digest`、`field catalog`、`manifest`、`follow-up gate` 为中心，明确不定义 tool calling、完整 agent runtime、transport、registry 或自动执行动作。
- 深度研究报告：将 CAP 定位为“语义描述、执行绑定与证据审计”的装配协议，核心对象扩展到 Artifact、Profile、Capability、Runtime、ResourceBinding、ServiceBinding、Policy、Run 和 Evidence。

因此，本报告讨论的不是某个字段设计对错，而是协议层级和命名边界的错位。

## 一、我们原先的隐含认知

现有文档的核心假设是：agent 面临的主要问题，是如何把复杂、巨大、敏感或危险的对象安全地放进模型上下文。

这个假设在当前文档中表现为：

- CAP 的中心产物是 `context digest`；
- source object 被拆成 field catalog；
- 每个 field 有预算、执行类别、trust class 和 redaction；
- digest manifest 记录哪些字段被包含、拒绝、降级或隐藏；
- 模型只能通过 field ID 提出 follow-up；
- gate 在后续提取前做预算、权限、指纹和隐私检查；
- tool calling、agent runtime、transport、registry、自动执行动作都被排除在 v0.1 外。

这套思路本身是清晰的。它解决的是“模型如何安全读取对象”，不是“agent 如何可靠执行科研任务”。

## 二、最新研判指出的真实问题

深度研究报告把 CAP 放在更大的科学计算和工程 agent 场景中审视。它指出，真实 agent 环境中的“上下文”不是单一文本对象，而至少包括五类对象：

- 数据对象；
- 执行环境；
- 资源约束；
- 外部服务；
- 权限边界。

在这个问题设定下，agent 需要回答的不只是“模型看到了什么”，还包括：

- 数据是什么，服从什么 schema 或 profile；
- 哪个 capability 可以处理它；
- capability 需要什么 runtime；
- runtime 绑定到本地、容器、WASI、集群还是远程执行后端；
- 需要多少 CPU、内存、GPU、时间、网络和存储；
- 需要哪些外部 API、对象存储、模型服务、许可证服务或数据库；
- 谁在什么条件下有权计划、绑定和执行；
- 一次 run 产生了哪些输入、输出、日志、签名、attestation 和 provenance；
- 结果能否被归档、复核和复现。

这说明：如果 CAP 要成为“机器可操作研究对象装配协议”，现有 `context digest` 只是其中一个 artifact，而不是协议核心。

## 三、认知差错的本质

### 1. 把局部机制误认为全局协议

我们设计出了一个相当合理的 digest 机制，然后把它命名为 `Context Assembly Protocol`。问题在于，“assembly” 在科学计算 agent 场景中天然指向跨层装配，而不只是 prompt context assembly。

局部机制的成功掩盖了全局问题的缺失：

- digest 能解释模型看到什么；
- 但不能解释任务在哪里跑；
- 不能解释运行依赖如何绑定；
- 不能解释外部服务如何治理；
- 不能解释完整 provenance 如何生成；
- 不能解释跨机构、跨 runtime、跨 profile 如何互操作。

### 2. 把“可引用上下文证据”误认为“可复现实验证据”

当前 manifest 能证明某个 field 是否进入 digest。它不能证明一个科学结果如何产生。

这两种 evidence 的层级不同：

| 证据类型 | 当前文档能力 | 大 CAP 需要 |
|---|---|---|
| Context evidence | 字段是否进入模型上下文，模型是否引用了合法 field ID | 当前文档基本覆盖 |
| Run evidence | 输入、参数、执行体、runtime、资源、外部服务、输出、日志、签名和 provenance | 当前文档基本未覆盖 |

因此，当前 manifest 应改称 `DigestManifest`。它不能承担 `RunEvidence` 或 `Provenance` 的职责。

### 3. 把“读对象的安全边界”误认为“执行任务的安全边界”

当前 gate 管的是 follow-up context extraction：模型能否继续请求某个字段、某个 level、某个预算。

但大 CAP 需要治理的是 plan、bind、execute、write、mutate、publish 等动作。它至少需要区分：

- visibility permission：能否发现；
- planning permission：能否放进计划；
- execution permission：能否在当前 principal、数据域、预算域和 runtime 下执行；
- evidence permission：谁能查看日志、输出和 provenance。

这不是把当前 gate 加几个字段就能解决的。它需要独立的 policy decision model。

### 4. 把 assembler capability 误称为 executable capability

当前 `Capability Discovery` 实际上描述的是 assembler 支持哪些 digest 特性，例如 `manifestV1`、`fieldCatalog`、`followupRequests`。

深度研究报告中的 `Capability` 是机器可调用能力，必须声明输入、输出、side effects、runtime、resource hints、secrets、external services、policy refs 和错误语义。

这两个概念同名但不同层。如果不拆开，会直接导致规范误读：

| 当前概念 | 更准确命名 | 上层 CAP 概念 |
|---|---|---|
| Capability Discovery | Assembler Feature Discovery | Capability Catalog / Capability Manifest |
| Field | ContextField | Capability input/output 可能引用的 artifact view |
| Context Pack | Digest Pack / Reader Pack | Skill 或 Profile 不能被它替代 |
| Gate | Follow-up Gate | Policy Decision Point 的局部应用 |

### 5. 把“避开现有标准竞争”误解为“不需要上层装配”

当前文档为了避免重造 MCP、Skills、CWL、OCI、Kubernetes，选择把 transport、runtime、tool calling、registry 都排除出去。这个判断在 digest 层是对的。

但如果 CAP-Core 的目标是跨层装配，那么它不能假装这些层不存在。正确做法不是替代它们，而是定义如何引用、绑定和审计它们：

- MCP 做交互式发现和调用入口；
- Skills 做人类可维护的工作说明；
- CWL 做批处理工作流 profile；
- RO-Crate 做研究对象封装；
- OCI/WASI/Kubernetes/REAPI 做执行绑定；
- Sigstore/in-toto/SPDX/CycloneDX 做可信供应链和证据；
- OPA/Cedar 做外部策略判定。

CAP-Core 的价值是把这些标准接起来，而不是把它们排除在认知框架外。

## 四、为什么这个差错严重

这个偏差会带来五类后果。

第一，**定位会误导实现者**。如果实现者以为当前 CAP 已经覆盖 agent scientific execution，他们会在 runtime、resource、service、policy、provenance 上各自扩展，最后互操作失败。

第二，**验收标准会错位**。当前成功标准是 field ID、redaction、digest manifest 和 follow-up gate；大 CAP 的成功标准是描述、发现、编排、授权、执行、审计和归档闭环。

第三，**安全模型会过窄**。当前模型主要防数据泄露、prompt injection 和未授权字段提取；大 CAP 还要防供应链篡改、凭据泄露、权限扩大、运行时逃逸、数据外流、证据伪造和拒绝钱包攻击。

第四，**生态策略会失真**。如果 CAP 被描述成 standalone standard，容易和 MCP、Skills、CWL、RO-Crate、OCI、Kubernetes 处在同一平面竞争。正确策略是适配和装配。

第五，**版本治理会失控**。digest 层字段、领域 profile、runtime binding、policy model、evidence model 如果混在一个 schema 里演化，后续兼容性会非常脆弱。

## 五、正确的认知框架

### 1. CAP-Core 是跨层装配契约

CAP-Core 的核心问题不是“如何生成一段更好的上下文文本”，而是：

> 如何把机器可操作研究对象、可执行能力、运行绑定、资源约束、授权决策和证据链装配成一个可发现、可组合、可执行、可追责的契约。

它的最小元模型应包括：

| 实体 | 职责 |
|---|---|
| `Artifact` | 数据、代码、模型、配置、日志、镜像、文档等对象 |
| `Profile` | 领域或执行约束，例如 BIDS、CWL batch、ML experiment |
| `Capability` | 机器可调用能力，声明输入、输出、副作用和错误语义 |
| `Skill` | 面向 agent 或人的工作说明，引用 capability |
| `Runtime` | 本地进程、OCI、WASI、Kubernetes、HPC、REAPI 等执行边界 |
| `ResourceBinding` | CPU、内存、GPU、时限、网络、存储、地域 |
| `ServiceBinding` | 外部 API、数据库、对象存储、模型服务、许可证服务 |
| `Policy` | principal、action、resource、condition 和 decision |
| `Run` | 一次执行实例，含状态、输入、输出、日志和时间线 |
| `Evidence` | provenance、signature、attestation、SBOM、环境锁 |

### 2. CAP-Digest 是 CAP-Core 下的一种 artifact/profile

当前文档应被重新理解为：

> CAP-Digest 定义如何把一个 artifact view 安全地渲染成模型可读的上下文证据，并记录 digest 级别的选择、删减、脱敏、失败和 follow-up 请求。

它负责的问题包括：

- source object inspection；
- field catalog；
- context budget；
- digest text；
- data fencing；
- redaction；
- digest manifest；
- field-level evidence；
- follow-up request；
- follow-up gate。

它不负责：

- capability execution；
- runtime scheduling；
- full provenance；
- global registry；
- external service governance；
- cross-organization authorization；
- workflow semantics；
- software supply-chain attestation。

### 3. “证据”要分两层

正确框架中至少要区分两种 evidence：

```text
RunEvidence
  证明一次执行如何发生
  包含输入、参数、执行体、runtime、资源、服务、输出、日志、签名、provenance

DigestEvidence
  证明模型看到了什么
  包含 selected fields、rejected fields、redactions、caveats、field citations
```

DigestEvidence 可以引用 RunEvidence。比如，某个 digest field 展示的是一次 run 的输出摘要，那么它应该指向上层 run evidence，而不是自己承担完整复现证明。

### 4. “权限”要分三段

正确权限模型不是单一 gate，而是分段决策：

| 阶段 | 问题 | 示例 |
|---|---|---|
| Discover | 能否知道它存在 | 能否看到某 capability 或 artifact metadata |
| Plan | 能否把它纳入计划 | 能否把患者数据绑定到某分析 workflow |
| Execute | 能否实际运行 | 能否使用 GPU、外网、密钥或写入对象存储 |
| Inspect | 能否查看结果证据 | 能否读取 logs、outputs、provenance、digest |

当前 follow-up gate 只覆盖 Inspect 的一个子场景：能否继续读取更多上下文。

### 5. 与现有标准的关系应是装配，不是替代

正确认知框架中，CAP-Core 不重新发明已有成熟标准，而是定义如何引用它们：

| 标准 | 在正确框架中的位置 |
|---|---|
| MCP | 交互式发现、调用和 agent 会话入口 |
| Agent Skills | 人类可写的任务说明和 progressive disclosure 包装 |
| CWL | 批式工作流 profile 和命令行工具语义 |
| RO-Crate | 研究对象归档和交换封装 |
| OCI | 软件执行体和镜像分发 |
| WASI | 细粒度 sandbox capability model |
| Kubernetes/HPC | 调度和资源执行后端 |
| REAPI | 远程动作执行、CAS、日志流和缓存 |
| Sigstore/in-toto | 签名、透明日志、供应链 attestation |
| SPDX/CycloneDX | SBOM 和依赖透明度 |
| OPA/Cedar | 策略判定和授权逻辑 |

CAP-Core 的独特价值是跨层 contract：一个 capability 不只说“我能做什么”，还说“我处理什么 artifact，在什么 runtime 下跑，需要什么资源和权限，调用了哪些服务，最后能留下什么证据”。

## 六、对现有文档的重新解释

现有 `cap-docs` 不需要推倒，但需要改名和降级。

| 现有文档概念 | 正确认知中的位置 | 建议 |
|---|---|---|
| CAP | CAP-Digest 或 Context Digest Profile | 不再称为完整 standalone CAP |
| SourceRef | Artifact 的局部 view 或 host-scoped reference | 保留，但说明不是全局 artifact identity |
| Field | ContextField | 保留，避免与 Capability 混淆 |
| Digest | DigestArtifact | 保留，作为 CAP-Core artifact |
| Manifest | DigestManifest | 改名，避免冒充 RunEvidence |
| Evidence validation | Digest citation validation | 保留，但明确不证明 claim truth 或 run reproducibility |
| Gate | Follow-up Gate | 保留，说明只是 context inspection gate |
| Context Pack | Digest Pack / Reader Pack | 保留，但不等同于 Skill |
| Capability Discovery | Assembler Feature Discovery | 必须改名，避免和 executable capability 冲突 |

## 七、推荐的新分层架构

```text
Layer 0: External Standards
  MCP, Skills, CWL, RO-Crate, OCI, WASI, Kubernetes, REAPI,
  Sigstore, in-toto, SPDX, CycloneDX, OPA, Cedar

Layer 1: CAP-Core
  Artifact graph
  Profile registry
  Capability manifest
  Runtime and resource binding
  Service binding
  Policy decision record
  Run lifecycle
  Evidence and provenance envelope

Layer 2: CAP Profiles and Bindings
  CAP-over-MCP
  Skills-frontmatter binding
  CWL batch profile
  RO-Crate archive profile
  OCI/WASI/K8s/REAPI runtime bindings
  Domain profiles such as BIDS, bioinformatics, ML experiment

Layer 3: CAP-Digest
  SourceRef
  Field catalog
  Budget allocator
  Digest text
  DigestManifest
  Redaction
  Caveats
  Follow-up gate
```

这套分层让当前工作变得有位置，而不是被否定。

## 八、后续修正路径

建议按四步修正。

### 第一步：立刻修正定位

把当前 README 的定位从：

```text
Scope: standalone standard
```

改为：

```text
Scope: CAP-Digest profile / context evidence layer
```

并在开头说明：本文档集定义 CAP 的上下文摘要层，不定义 CAP-Core 的完整研究对象装配模型。

### 第二步：重命名冲突术语

优先改：

- `Capability Discovery` -> `Assembler Feature Discovery`
- `Manifest` -> `DigestManifest`
- `Evidence` -> `DigestEvidence`
- `Gate` -> `Follow-up Gate`
- `Context Pack` -> `Digest Pack` 或 `Reader Pack`

这些改名可以显著降低误读。

### 第三步：另起 CAP-Core 草案

新建 CAP-Core 文档，不要把 runtime、policy、run evidence 直接塞进当前 digest spec。

CAP-Core 草案应先写：

- problem statement；
- ontology；
- lifecycle；
- relation to existing standards；
- minimal manifest shape；
- conformance boundaries；
- MVP profile。

### 第四步：定义 CAP-Digest 与 CAP-Core 的接口

关键接口是：

```text
RunEvidence -> DigestArtifact
Artifact -> ArtifactView -> SourceRef
Capability output -> Digest field source
Policy decision -> Follow-up gate input
Profile constraint -> field availability and redaction policy
```

这样当前 digest 层可以成为大 CAP 的可证明上下文出口。

## 九、判断新设计是否走偏的检查表

后续每添加一个概念，都先问：

1. 它属于 CAP-Core、CAP-Digest、Profile、Binding，还是外部标准？
2. 它描述的是 artifact、capability、runtime、resource、service、policy、run，还是 digest field？
3. 它是在证明“模型看到了什么”，还是证明“一次执行如何发生”？
4. 是否已经有 MCP、CWL、RO-Crate、OCI、Kubernetes、WASI、REAPI 等标准覆盖？
5. CAP 是要引用它、绑定它、审计它，还是不该碰它？
6. 如果没有 reference implementation，这个字段是否应该进入 core？
7. 如果这个字段只服务某个学科，是否应放入 profile？
8. 如果这个字段只服务模型上下文读取，是否应留在 CAP-Digest？

只要坚持这个检查表，就能避免再次把局部机制升级成全局本体。

## 十、结论

这次认知差错可以概括为：

> 我们把“如何安全生成模型上下文”误认为“如何装配机器可操作研究对象”。

正确认知应当是：

> CAP-Core 负责跨层装配；CAP-Digest 负责上下文证据。前者定义研究对象、能力、运行、资源、服务、权限和证据的契约；后者定义模型看到什么、为什么看到、没看到什么、还能否安全追问。

因此，当前工作不是作废，而是需要重新定位：

- 保留 digest 机制；
- 降级为 CAP-Digest；
- 另起 CAP-Core；
- 用 profile 和 binding 接入 MCP、Skills、CWL、RO-Crate、OCI、WASI、Kubernetes、REAPI 和可信供应链工具；
- 用 evidence 分层避免把 field citation 误当成 scientific provenance。

这样 CAP 才不会成为“另一个更大的标准”，而会成为把现有标准接成真实 agent 科学计算闭环的装配层。

---

## 注记（2026-07-05 重构同步）

本备忘引用的旧顶层 README `Scope: standalone standard` 已于 2026-07-05 重构中更新为 `Scope: CAP-Digest profile (CAP-Core reserved)`，原 01–12 规范文档已迁入 `specs/digest/` 并按 CAP-Digest 口径统一术语（`Manifest` → `DigestManifest`、`Evidence` → `DigestEvidence`、`Context Pack` → `Digest Pack`），13/14 号文档降级为 `notes/` 下设计备忘。本备忘正文结论不受影响。
