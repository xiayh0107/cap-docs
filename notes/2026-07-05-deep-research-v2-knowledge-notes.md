# Deep Research v2 知识留存笔记

> Status: analysis · Non-normative · Source: `/Users/xiayh/Projects/ai-spec/review/deep-research-report_v2.md` · Date: 2026-07-05

## 处理原则

`deep-research-report_v2.md` 的总体结论仍然受到同一个认知偏差影响：它把当前 `cap-docs` 所定义的上下文摘要层，推向了更大的“机器可操作研究对象装配协议”。

因此，这份笔记不采纳 v2 对当前 CAP 的最终定位结论，而是把其中有价值的信息拆出来，作为未来做 **CAP-Core / 上层装配协议** 调研时的知识素材。

使用方式：

- 可以学习：标准生态、概念边界、用例排序、MVP 权衡、风险清单、治理路线。
- 暂不采纳：把当前 CAP-Digest 直接升级为完整 assembly protocol 的结论。
- 暂不执行：v2 里关于 Core Manifest、Runtime Binding API、CAP 标准化路线的具体落地建议。
- 后续需要：在认知框架纠正后，重新做一次针对 CAP-Core 的调研和引用核验。

## 一、v2 中值得保留的核心洞察

### 1. Agent 场景里的“上下文”可以被更广义地理解

v2 提醒我们：在真实科研和工程 agent 场景中，context 不只是 prompt 里的文本、图片或 tool 参数。

更广义的 context 可能包括：

- 数据对象；
- 执行环境；
- 依赖闭包；
- 权限边界；
- 状态快照；
- 可执行入口；
- 可追溯证据。

这对未来 CAP-Core 很重要，但对当前 CAP-Digest 只能作为背景知识。当前 CAP-Digest 处理的是“模型可见上下文证据”，不是完整执行上下文。

### 2. 现有生态不是空白，而是分层分散

v2 的标准扫描有价值。它指出现有生态已经分别覆盖了多个层面：

| 层面 | 代表标准/系统 | 可复用知识 |
|---|---|---|
| Agent 连接 | MCP | 连接外部资源、tools、prompts；适合作为动态入口，不是完整装配模型 |
| 程序性知识 | Agent Skills | 渐进式加载说明、脚本和资源；适合人类可维护包装，不是严格执行契约 |
| 语义图 | JSON-LD | 表达资源图、引用和本体映射；适合语义层，但不定义执行 |
| 科研对象包装 | RO-Crate / Workflow Run RO-Crate | 聚合数据、代码、工作流、provenance；适合静态归档和交换 |
| 领域数据结构 | BIDS | 证明领域 profile 很重要；不应被通用 core 取代 |
| 工作流 | CWL | 声明式命令行工具和 workflow；适合 batch profile |
| 环境封装 | Docker / OCI / Nix / WASI | 处理运行环境、镜像、可复现构建和沙箱；CAP 应引用而非替代 |
| 调度执行 | Kubernetes / HPC / REAPI | 处理资源调度和远程执行；适合作为 runtime binding |
| 实验谱系 | W3C PROV / MLflow / DataLad | 处理 provenance、实验 lineage、版本化数据和代码 |
| 证据与供应链 | in-toto / Sigstore / SPDX / CycloneDX | 处理 attestation、签名、SBOM 和透明度 |
| 执行观测 | OpenTelemetry | 处理 trace、metrics、logs；可作为 run evidence 的输入 |
| 大数据面 | Arrow Flight / 对象存储 | 处理大对象和跨进程数据流；提示控制面与数据面要分离 |

正确吸收方式：这些知识应进入 CAP-Core 的生态图和兼容性章节，而不是塞进当前 CAP-Digest schema。

### 3. “复用优先”是正确原则

v2 反复强调：CAP 不应重新发明工作流语言、容器格式、权限系统、metadata ontology、传输协议或审计框架。

这个原则值得保留。未来如果做 CAP-Core，应遵守：

- 语义层复用 JSON-LD / PROV / CodeMeta / Bioschemas；
- 包装层复用 RO-Crate；
- 运行环境复用 OCI / WASI / Nix；
- 工作流 profile 复用 CWL；
- 证据层复用 in-toto / Sigstore / SPDX / CycloneDX；
- 权限层桥接 OAuth/OIDC、capability token、组织策略系统；
- 大对象传输走对象存储、Arrow Flight 或专用数据面。

这也支持我们已经得出的纠偏结论：大 CAP 的价值是装配 existing standards，不是替代它们。

## 二、v2 中可复用的问题框架

v2 给出的五个第一性问题值得保留：

```text
1. 我面对的是什么对象，它在哪里？
2. 我要在什么环境里操作它？
3. 我被允许做什么？
4. 我实际做了什么？
5. 别人如何验证这一切？
```

纠偏后的解释应是：

| 问题 | 属于哪一层 |
|---|---|
| 模型看到了什么、引用了什么、还能请求什么 | CAP-Digest |
| 对象是什么、如何标识、如何绑定到执行 | CAP-Core |
| capability 在什么 runtime 中运行 | CAP-Core / Runtime Binding |
| 权限如何授予、决策如何审计 | CAP-Core / Policy Binding |
| run 如何留下可验证证据 | CAP-Core / Evidence Binding |

这组问题可以作为未来 CAP-Core problem statement 的骨架。

## 三、v2 的用例排序可作为参考，不作为当前目标

v2 给出了一组推荐优先级。它们对上层 CAP-Core 有参考价值。

| 推荐优先级 | 用例 | 可保留价值 | 注意事项 |
|---|---|---|---|
| P0 | 科研复现 | 数据、代码、环境、参数、证据需要可交换 | 不应成为 CAP-Digest 的成功标准 |
| P0 | 可解释性与审计 | 需要解释 agent 对什么对象、按什么权限、在什么环境下做了什么 | 当前 Digest 只能解释模型看到什么 |
| P0 | 跨运行时执行 | 本地、容器、集群、云之间迁移困难 | 属于 Runtime Binding，不属于 digest spec |
| P1 | 长任务与重入 | checkpoint、状态、权限快照需要绑定 | 属于 Run / State model |
| P1 | 分布式计算与数据就近 | 大对象不能内联到 prompt | 支持“引用而非复制”的设计原则 |
| P1 | 跨域协作 | 不同学科有不同对象和证据语言 | 支持 Core + Profile 分层 |
| P2 | 代理间协同 | 多 agent 共享上下文契约 | 后续方向，不宜进入 MVP |
| P2 | 教学、审稿与合规交付 | 需要可审阅、可运行、可验证的研究对象 | 适合做 adoption case |

处理结论：这些用例应进入“未来 CAP-Core 调研候选”，不应倒推当前 CAP-Digest 改范围。

## 四、v2 的标准边界知识

### MCP

可保留知识：

- MCP 强在 agent 与外部资源、工具、prompt 的连接；
- MCP 适合动态发现和调用；
- MCP 本身不是研究对象封装、运行时绑定或 provenance 标准；
- 未来 CAP-Core 可以提供 CAP-over-MCP binding。

不要误用：

- 不要把 MCP 当成 CAP-Core 的替代物；
- 不要把当前 CAP-Digest 的 follow-up gate 等同于 MCP tool execution。

### Agent Skills

可保留知识：

- Skills 擅长渐进式披露程序性知识；
- `SKILL.md`、scripts、references、assets 的组合对 agent 工程友好；
- Skills 可以作为人类可维护入口。

不要误用：

- Skills 不是机器可验证 capability contract；
- `allowed-tools` 这类字段不能承担完整安全模型；
- Context Pack / Digest Pack 不应被称为 Skill。

### JSON-LD

可保留知识：

- JSON-LD 适合表达资源身份、引用、图结构和语义映射；
- 它可以作为 CAP-Core semantic graph 的候选载荷。

不要误用：

- JSON-LD 不等于执行语义；
- 需要 JSON Schema / SHACL / profile rules 做验证；
- 当前 CAP-Digest 不必被强行改成 JSON-LD。

### RO-Crate 与 Workflow Run RO-Crate

可保留知识：

- RO-Crate 是静态研究对象包装层的强近邻；
- Workflow Run RO-Crate 已经覆盖工作流输入、输出、代码和 execution provenance；
- 适合做 CAP-Core archive/profile binding。

不要误用：

- RO-Crate 不解决 live runtime binding；
- 不应把 CAP-Digest 直接做成 RO-Crate 的替代物。

### CWL

可保留知识：

- CWL 是批处理工作流和命令行工具描述标准；
- 可以成为 workflow/batch profile；
- 它解决“如何跑流程”的一部分。

不要误用：

- CWL 不解决 agent 交互式上下文、权限治理和完整审计；
- CAP-Core 应适配 CWL，而不是重写 CWL。

### OCI、WASI、Kubernetes、Nix

可保留知识：

- OCI 提供镜像和分发；
- WASI 提供更细粒度的能力式沙箱；
- Kubernetes/HPC 处理调度和资源；
- Nix 体现声明式、可复现环境的思想。

不要误用：

- 容器不等于完整复现；
- 调度器不关心研究对象语义；
- CAP-Core 应保存不可变引用、digest、platform constraints 和证据，而不是定义自己的 runtime。

### W3C PROV、MLflow、DataLad

可保留知识：

- PROV 可描述 entity、activity、agent、derivation、responsibility；
- MLflow 对 ML experiment、lineage、model registry 有参考价值；
- DataLad 对分布式数据、版本、来源关系有参考价值。

不要误用：

- 当前 DigestEvidence 不是 PROV；
- MLflow 是 ML profile 候选，不是通用 core；
- DataLad 的思想可借鉴，但不应硬依赖。

### in-toto、Sigstore、SPDX、CycloneDX、OpenTelemetry

可保留知识：

- in-toto / DSSE / Sigstore 适合 attestation 与签名证据；
- SPDX / CycloneDX 适合 SBOM 和依赖透明度；
- OpenTelemetry trace/log/metric 可以作为 run evidence 的输入。

不要误用：

- 日志不等于证据；
- 签名也不等于语义正确；
- 供应链证据是 CAP-Core Evidence 的一部分，不属于 CAP-Digest core。

## 五、v2 中值得保留的设计原则

### 1. 不定义通用对象 ABI

v2 里最值得保留的反直觉建议是：不要定义通用跨语言对象内存表示。

正确方向是定义对象信封，而不是对象内核：

```text
Object envelope:
  id
  type/profile
  schema
  locator
  digest
  codec
  available operations
  binding mode
```

对象内部值可以由 profile 决定，例如 table、array、workflow、model、image、database stream。

这条原则对未来 CAP-Core 非常重要，也能保护当前 CAP-Digest 不被拖进分布式对象系统。

### 2. 控制面和数据面分离

v2 强调大对象不能内联进 prompt 或 manifest。

可保留原则：

- manifest 中保存身份、schema、locator、digest、policy、binding；
- 大对象走对象存储、文件系统、stream、Arrow Flight 或数据库；
- 默认引用和只读挂载，避免复制和隐式 materialization。

这也和当前 CAP-Digest 的安全读对象思想兼容：digest 只呈现必要上下文，不搬运全部数据。

### 3. Core + Profile 分层

v2 支持 `CAP Core + Domain Profiles`。

纠偏后应理解为：

- CAP-Core 定义跨域稳定对象：Artifact、Capability、Runtime、Policy、Run、Evidence；
- CAP-Digest 是一个 context evidence profile；
- BIDS、CWL、ML experiment、simulation 等应是领域 profile；
- profile 承担领域语义，不进入 core。

### 4. Manifest + Binding API 双层

v2 提出静态 `Assembly Manifest` 与动态 `Runtime Binding API` 双层。

可保留为未来 CAP-Core 候选架构：

- 静态层：可签名、可缓存、可归档、可交换；
- 动态层：resolver、runtime、policy、binding、status、logs。

但它不适合直接套到当前 CAP-Digest。当前 digest 的 manifest 是 `DigestManifest`，不是 Assembly Manifest。

### 5. 证据链必须早设计

v2 的证据意识值得保留：

- run evidence 应记录输入、环境、权限、执行过程、输出、签名和 provenance；
- evidence 应可验证、可归档、可引用；
- attestation、SBOM、trace、PROV 可以组合成 evidence bundle。

纠偏后应区分：

```text
DigestEvidence: 模型看到了什么
RunEvidence: 执行如何发生
SupplyChainEvidence: 执行体和依赖是否可信
```

## 六、v2 的技术取舍表，可作为未来 CAP-Core 备忘

| 设计点 | v2 建议 | 纠偏后的状态 |
|---|---|---|
| 数据模型 | 图模型为核心，提供树状视图 | 可作为 CAP-Core 候选，不影响当前 CAP-Digest |
| 接口 | Manifest + Binding API 双层 | 可作为未来上层架构 |
| 序列化 | JSON-LD + JSON Schema，性能通道可选 Protobuf/gRPC | 需后续调研核验；当前不执行 |
| 发现 | 去中心发现优先，辅以注册表 | 可作为未来 registry 讨论 |
| 权限 | 资源级 capability grant + OAuth/OIDC 桥接 | 可作为 policy model 候选 |
| 版本 | 语义版本 + 不可变 digest 双轨 | 值得保留 |
| 沙箱 | OCI 为主，WASI 为补充 | 未来 runtime binding 方向 |
| 签名 | JCS digest + DSSE/in-toto + Sigstore | 未来 evidence 方向 |
| 数据传输 | 小元数据内联，大对象引用 | 值得保留 |
| 语义扩展 | Core + Domain Profiles | 值得保留 |

## 七、v2 的原型路线，处理为参考选项

v2 提出两个原型方向。

### 方案 A：重装配、强复现

特点：

- CAP 控制 runtime assembly；
- manifest 引用 OCI/WASI；
- 资源通过挂载、secret、service handle 接入；
- 执行过程产生 trace、PROV、attestation；
- 适合科研复现和合规审计。

保留价值：

- 可以作为未来 CAP-Core “强模式”的目标；
- 有利于验证跨后端重放和证据完整性。

暂不执行原因：

- 接入成本高；
- 容易变成另一套平台；
- 不适合用来改当前 CAP-Digest。

### 方案 B：轻装配、快接入

特点：

- 在 MCP、skills、HTTP、对象存储、现有调度器之上增加轻量 manifest；
- 资源引用、schema、locator、digest、capability grant 和最小 provenance；
- 运行时仍由现有平台处理。

保留价值：

- 适合作为未来 CAP-Core adoption 路线；
- 先证明 assembly contract 价值，再逐步增强证据和执行。

暂不执行原因：

- 如果没有明确 CAP-Core / CAP-Digest 分层，仍会污染当前规范边界。

纠偏后的判断：

```text
未来 CAP-Core 可以先做 B，逐步走向 A。
当前 CAP-Digest 不参与这个选择，只定义模型上下文证据层。
```

## 八、v2 中需要隔离的结论

以下判断有启发，但暂时不能采纳为当前规范方向：

1. **“CAP 值得做，因为它能把对象 + 环境 + 权限 + 证据装配成统一上下文单元。”**  
   这适用于未来 CAP-Core，不适用于当前 CAP-Digest 的定位。

2. **“CAP 应定义 Assembly Manifest 与 Runtime Binding API。”**  
   这是上层协议候选，不是当前 digest spec 的改造目标。

3. **“MVP 应优先做科研复现、跨运行时重放、审计与解释性。”**  
   这是 CAP-Core MVP 的候选，不是 CAP-Digest 的 MVP。

4. **“CAP 暂时作为项目代号，不作为最终标准名。”**  
   命名风险值得记录，但不应在当前阶段主导技术重构。

5. **“CAP 是上下文装配层标准。”**  
   这句话需要拆解：CAP-Core 可以是装配层；CAP-Digest 是上下文证据层。

## 九、从 v2 萃取出的未来调研问题

后续做纠偏后的 CAP-Core 调研时，应重点验证：

1. JSON-LD + JSON Schema + SHACL 的组合是否适合作为 CAP-Core manifest 的语义与验证基础？
2. RO-Crate / Workflow Run RO-Crate 与 CAP-Core 的最小差异到底是什么？
3. W3C PROV 能否覆盖 CAP-Core RunEvidence，哪些字段需要扩展？
4. in-toto / DSSE / Sigstore 如何与 run evidence、artifact digest、SBOM 连接？
5. Capability grant 应采用能力令牌、OAuth/OIDC scope、Zanzibar-style relation graph，还是组合模型？
6. Runtime binding 应只定义抽象接口，还是要规定 OCI/WASI/K8s/REAPI 的最小适配字段？
7. MCP binding 应暴露 manifest、resolver、run status、evidence，还是只暴露 capability catalog？
8. Domain profile 的治理边界如何定义，避免 core 被领域字段污染？
9. Control plane / data plane separation 的最小必需字段是什么？
10. CAP-Core 与当前 CAP-Digest 的接口应如何设计，才能让 digest 成为 run evidence 的可读出口？

这些问题需要新的调研，不应直接用 v2 的结论代替。

## 十、当前可执行的整理动作

目前只建议做知识整理，不做规范重构。

已从 v2 留存的可用资产：

- 生态地图；
- 用例优先级；
- 复用优先原则；
- Core + Profile 思路；
- Manifest + Binding API 候选架构；
- 对象信封而非对象 ABI 的原则；
- 控制面与数据面分离原则；
- RunEvidence / SupplyChainEvidence 的素材；
- 原型 A/B 路线；
- 标准化和治理工作组设想；
- 命名风险提醒。

当前不应做的动作：

- 不把当前 CAP-Digest 改成 JSON-LD assembly manifest；
- 不把 runtime、resource、service、policy、attestation 塞进现有 digest spec；
- 不把 v2 的 P0/P1/P2 用例当成当前 CAP-Digest 的验收测试；
- 不把 v2 的 “CAP is assembly layer” 结论直接写进 README；
- 不开始设计 Runtime Binding API，直到 CAP-Core 定位单独完成。

## 十一、结论

`deep-research-report_v2.md` 的结论层需要隔离，但知识层值得保留。

最准确的处理方式是：

```text
v2 = 未来 CAP-Core 的知识素材库
不是当前 CAP-Digest 的方向判决书
```

它给了我们一张有用的生态地图：MCP、Skills、JSON-LD、RO-Crate、CWL、OCI、WASI、Kubernetes、PROV、MLflow、DataLad、in-toto、Sigstore、SPDX、CycloneDX、OpenTelemetry、Arrow Flight 等分别解决不同层的问题。

后续真正要做的，是在认知框架纠正后，重新围绕 CAP-Core 做一次调研：先定义问题和层级，再核验证据和标准边界，最后决定哪些知识进入 core、哪些进入 profile、哪些只作为 binding。
