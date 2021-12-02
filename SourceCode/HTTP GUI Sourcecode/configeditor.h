#ifndef CONFIGEDITOR_H
#define CONFIGEDITOR_H

#include <QWidget>

QT_BEGIN_NAMESPACE
namespace Ui { class ConfigEditor; }
QT_END_NAMESPACE

class ConfigEditor : public QWidget
{
    Q_OBJECT

public:
    ConfigEditor(QWidget *parent = nullptr);
    ~ConfigEditor();

private slots:
    void on_save_button_clicked();

private:
    Ui::ConfigEditor *ui;
    void loadTextFile();
};
#endif // CONFIGEDITOR_H
