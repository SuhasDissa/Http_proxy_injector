#include "configeditor.h"
#include "ui_configeditor.h"
#include <QSettings>

ConfigEditor::ConfigEditor(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::ConfigEditor)
{
    ui->setupUi(this);
    loadTextFile();

}

ConfigEditor::~ConfigEditor()
{
    delete ui;
}


void ConfigEditor::on_save_button_clicked()
{
    QSettings settings("./settings.ini", QSettings::IniFormat);
    settings.beginGroup("/ssh");
    QString host = ui->host_edit->text();
    QString port = ui->port_edit->text();
    QString uname = ui->uname_edit->text();
    QString pwd = ui->pwd_edit->text();
    settings.setValue("/host", host);
    settings.setValue("/port", port);
    settings.setValue("/username", uname);
    settings.setValue("/password", pwd);
    settings.endGroup();
    settings.beginGroup("/config");
    QString payload = ui->payload_edit->toPlainText();
    settings.setValue("/payload", payload);
    settings.endGroup();
    settings.beginGroup("/sni");
    QString sni = ui->sni_edit->text();
    settings.setValue("/server_name", sni);
    settings.endGroup();
}
void ConfigEditor::loadTextFile()
{
    QSettings settings("./settings.ini", QSettings::IniFormat);
    settings.beginGroup("/ssh");
    QString host = settings.value("/host").toString();
    QString port = settings.value("/port").toString();
    QString uname = settings.value("/username").toString();
    QString pwd = settings.value("/password").toString();
    //std::cout << qs.toUtf8().data();
    settings.endGroup();
    settings.beginGroup("/config");
    QString payload = settings.value("/payload").toString();
    settings.endGroup();
    settings.beginGroup("/sni");
    QString sni = settings.value("/server_name").toString();
    settings.endGroup();
    ui->host_edit->setText(host);
    ui->port_edit->setText(port);
    ui->uname_edit->setText(uname);
    ui->pwd_edit->setText(pwd);
    ui->sni_edit->setText(sni);
    ui->payload_edit->setPlainText(payload);
}

