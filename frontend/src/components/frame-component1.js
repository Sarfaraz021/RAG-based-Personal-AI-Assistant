// frontend\src\components\frame-component1.js
import styles from "./frame-component1.module.css";

const FrameComponent1 = () => {
  return (
    <div className={styles.rectangleParent}>
      <div className={styles.frameChild} />
      <div className={styles.frameParent}>
        <div className={styles.danysAssistantWrapper}>
          <h2 className={styles.danysAssistant}>DANY’s ASSISTANT</h2>
        </div>
        <img
          className={styles.separatorIcon}
          loading="lazy"
          alt=""
          src="/separator.svg"
        />
        <div className={styles.frameWrapper}>
          <div className={styles.rectangleGroup}>
            <div className={styles.frameItem} />
            <img
              className={styles.icroundAddIcon}
              loading="lazy"
              alt=""
              src="/icroundadd.svg"
            />
            <div className={styles.newChatWrapper}>
              <div className={styles.newChat}>New Chat</div>
            </div>
          </div>
        </div>
      </div>
      <div className={styles.regenerateResponseButtonWrapper}>
        <button className={styles.regenerateResponseButton}>
          <div className={styles.wrapperVector}>
            <img className={styles.vectorIcon} alt="" src="/vector.svg" />
          </div>
          <div className={styles.upgradeToPlus}>Upgrade to Plus</div>
        </button>
      </div>
    </div>
  );
};

export default FrameComponent1;
