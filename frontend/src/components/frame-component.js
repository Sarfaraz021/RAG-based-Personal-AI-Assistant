// frontend/src/components/frame-component.js
import styles from "./frame-component.module.css";

const FrameComponent = () => {
  return (
    <section className={styles.rectangleParent}>
      <div className={styles.frameChild} />
      <h1 className={styles.chatWithYour}>Chat with your docs</h1>
      <div className={styles.frameParent}>
        <div className={styles.frameWrapper}>
          <div className={styles.rectangleGroup}>
            <div className={styles.frameItem} />
            <div className={styles.rectangleContainer}>
              <div className={styles.frameInner} />
              <img className={styles.vectorIcon} alt="" src="/vector-1.svg" />
            </div>
          </div>
        </div>
        <div className={styles.containerParent}>
          <img
            className={styles.containerIcon}
            loading="lazy"
            alt=""
            src="/ellipse-137@2x.png"
          />
          <div className={styles.title} />
        </div>
      </div>
    </section>
  );
};

export default FrameComponent;
