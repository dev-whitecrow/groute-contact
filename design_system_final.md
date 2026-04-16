# ACTS29 디자인 시스템 가이드

이 문서는 ACTS29의 시각적 일관성과 실행 속도를 높이기 위한 가이드입니다. 모든 설계는 '명쾌함'과 '실행의 에너지'를 원칙으로 합니다.

---

## 1. Brand Assets

### A. Primary Color: ACT Mint
디지털/테크적 감성과 지적인 활력을 상징합니다.
- **HEX**: #00C4B4
- **적용**: 메인 CTA 버튼, 헤드라인 핵심 키워드 강조, 로고.

### B. Base Colors (베이스 컬러)
전문성을 높이기 위해 순수 블랙 대신 깊이 있는 그레이를 사용합니다.
- **Background**: #FFFFFF (Pure White)
- **Sub Background**: #F8F9FA (섹션 구분용 연한 그레이)
- **Body Text**: #2D3748 (Deep Slate Gray / 본문용)
- **Sub Text/Border**: #A0AEC0 (연한 테두리 및 비활성 텍스트용)

### C. Accent Color: Spark Yellow
아이디어의 반짝임과 따뜻한 에너지를 더합니다.
- **HEX**: #F5D11E
- **사용 규칙**: 글자색으로는 사용하지 않으며, 배지(Badge) 배경이나 아이콘 포인트로만 사용합니다. (노란색 배경 위 글자는 반드시 #2D3748 사용)

---

## 2. Design Principle

### 8px 여백 규칙 (Spacing System)
안정감 있는 레이아웃을 위해 모든 간격은 8의 배수를 사용합니다.
- **간격 단위**: 8, 16, 24, 32, 40, 48, 64, 80 (px)
- **적용**: 요소 간 간격, 섹션 상하 패딩, 카드 내부 여백 등.

### 에셋 사용 가이드 (Asset Guide)
- **사진**: '자연스러운 아이폰 사진(Candid iPhone Style)'을 원칙으로 합니다. 인위적인 포즈보다 자연광 아래의 생생한 현장감을 우선합니다.
- **아이콘**: 선의 두께가 일정한 단일 세트를 사용합니다. (추천: Lucide 또는 Phosphor Icons)

---

## 3. Typography (타이포그래피)

### 기본 폰트: Pretendard
```css
/* Fallback Font 설정 */
font-family: 'Pretendard', 'Apple SD Gothic Neo', 'Noto Sans KR', 'Malgun Gothic', sans-serif;
```

### 위계 및 크기 (Typography Scale)

| Level | Size | Weight | Line-height | 비고 |
| :--- | :--- | :--- | :--- | :--- |
| **H1** | 32px | Bold | 1.4 | 메인 타이틀 |
| **H2** | 24px | Bold | 1.4 | 섹션 타이틀 |
| **H3** | 18px | SemiBold | 1.5 | 카드/그룹 제목 |
| **Body** | 16px | Regular | 1.6 | 기본 본문 |
| **Caption** | 14px | Regular | 1.6 | 설명/주석/부가정보 |

---

## 4. Components (핵심 컴포넌트)

### 1) 버튼 (Button)
- **Primary**: 배경 #00C4B4, 글씨 #FFFFFF / SemiBold / 곡률 8px (핵심 행동)
- **Secondary**: 배경 #F8F9FA, 글씨 #2D3748 / Medium / 곡률 8px (보조 행동)
- **Common**: 상하 여백 16px, 좌우 여백 24px

### 2) 입력창 (Input Field)
- **Default**: 배경 #FFFFFF, 테두리 1px #A0AEC0, 여백 16px, 곡률 8px
- **Active**: 테두리 2px #00C4B4 (포커스 시 시각적 피드백)
- **Error**: 테두리 2px #FF4D4F, 하단에 동일 색상의 에러 메시지 노출

### 3) 카드 (Card)
- **Style**: 배경 #FFFFFF, 곡률 12px, 내부 여백 24px
- **Shadow**: `0px 4px 12px rgba(0, 0, 0, 0.05)` (매우 부드러운 그림자)
- **Gutter**: 카드와 카드 사이 간격은 16px 또는 24px로 고정

---

**디자인 팁**:
상세페이지 제작 시, 이 시스템을 지키는 것만으로도 "신뢰할 수 있는 전문가의 공동체"라는 인상을 줄 수 있습니다. 이제 이 가이드를 바탕으로 본격적인 실행에 들어갑시다!
